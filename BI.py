import pandas as pd
import os
import time
from datetime import datetime

# --- GERAÇÃO DE DADOS DINÂMICOS PARA TESTE ---

# O valor do timestamp muda a cada execução (a cada 5 minutos no seu cron)
# Isso garante que o conteúdo do CSV seja diferente, forçando o Git a commitar.
timestamp_atual = int(time.time())

# Criando scores dinâmicos para simular a atualização de 2 em 2 minutos (conceitualmente)
# Usamos o timestamp para gerar valores ligeiramente diferentes a cada rodada.
score_qualidade = (timestamp_atual % 100) / 10 + 85  # Ex: 85.0 a 94.9
score_inovacao = (timestamp_atual % 100) / 10 + 75   # Ex: 75.0 a 84.9
score_atendimento = 90.0 + (timestamp_atual % 10) / 100 # Ex: 90.00 a 90.09

# Data e hora da simulação da atualização
data_atualizacao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# --- CONSTRUÇÃO DO DATAFRAME ---

all_grades = []

# Novo dado a cada execução:
all_grades.append({
    "review_id": 1,
    "grade_name": "Qualidade do Produto",
    "score": score_qualidade, 
    "weight": 0.4,
    "last_updated": data_atualizacao # Adiciona o timestamp para provar a mudança
})

# Dado que simula a inserção de um novo item de avaliação:
all_grades.append({
    "review_id": 3,
    "grade_name": "Inovacao Tecnológica",
    "score": score_inovacao,
    "weight": 0.5,
    "last_updated": data_atualizacao
})

# Dado que simula um item com pouca variação:
all_grades.append({
    "review_id": 2,
    "grade_name": "Atendimento ao Cliente",
    "score": score_atendimento,
    "weight": 0.6,
    "last_updated": data_atualizacao
})

# Cria o DataFrame
grades_df = pd.DataFrame(all_grades)

# --- SALVAMENTO DO ARQUIVO CSV ---

# 1. Cria a pasta de destino (o caminho 'data' que está no seu workflow YAML)
os.makedirs("data", exist_ok=True)

# 2. Salva o CSV
grades_df.to_csv("data/dados_atualizados_feira.csv", index=False, encoding="utf-8-sig")