import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

senha = os.getenv("SENHA_REQUISICAO")
url_endpoint_login = os.getenv("URL_LOGIN")
url_endpoint_reviews = os.getenv("URL_REVIEWS")

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
        os.makedirs("data", exist_ok=True)
        grades_df.to_csv("data/dados_atualizados_feira.csv", mode='a', index=False, encoding="utf-8-sig")
        print("Arquivo atualizado com sucesso!")
    else:
        print(f"Erro ao buscar reviews: {reviews_response.text}")
else:
    print("Erro ao obter token de autenticação.")