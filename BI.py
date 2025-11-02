import requests
import os
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine, text

load_dotenv()

senha = os.getenv("SENHA_REQUISICAO")
url_endpoint_login = os.getenv("URL_LOGIN")
url_endpoint_reviews = os.getenv("URL_REVIEWS")

db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_CREDENTIAL")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")

numero_mapa = 13
login_data = {
    "username": f"expositor_project-uuid-{numero_mapa}@example.com",
    "password": senha
}
login_headers = {
    "accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded"
}

response = requests.post(url_endpoint_login, data=login_data, headers=login_headers)

if response.status_code == 200:
    token = response.json().get("access_token")
else:
    print(f"Erro ao autenticar: {response.text}")
    token = None

if token:
    reviews_headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {token}"
    }
    reviews_response = requests.get(url_endpoint_reviews, headers=reviews_headers)

    if reviews_response.status_code == 200:
        data = reviews_response.json()

        #Trazendo os dados da API (requisição)
        all_grades = []
        for review in data:
            for grade in review["grades"]:
                all_grades.append({
                    "review_id": review["id"],  
                    "grade_name": grade["name"],
                    "score": grade["score"],
                    "weight": grade["weight"]
                })

        grades_df = pd.DataFrame(all_grades)

        #Salvando os dados no banco
        engine = create_engine(f"postgresql+psycopg2://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}")

        with engine.begin() as conn:
            for i, row in grades_df.iterrows():

                #LÓGICA UPSERT - evita duplicação de dados -> lógisca semlhante ao CDC de atualização
                update_script = text("""
                    UPDATE grades_feira
                    SET score = :score, weight = :weight
                    WHERE review_id = :review_id AND grade_name = :grade_name
                """)
                
                result = conn.execute(update_script, row.to_dict())

                if result.rowcount == 0:
                    insert_script = text("""
                        INSERT INTO grades_feira (review_id, grade_name, score, weight)
                        VALUES (:review_id, :grade_name, :score, :weight)
                    """)
                    conn.execute(insert_script, row.to_dict())

        print("Dados salvos (UPSERT via UPDATE/INSERT) no PostgreSQL com sucesso!")

    else:
        print(f"Erro ao buscar reviews: {reviews_response.text}")
else:
    print("Erro ao obter token de autenticação.")