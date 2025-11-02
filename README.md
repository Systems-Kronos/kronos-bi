# 🤖 kronos-bi-view-feira

## Índice

- [📓 Sobre](#-sobre)
- [🚀 Tecnologias](#-tecnologias)
- [✨ Funcionalidades](#-funcionalidades)
- [⚙️ Instalação](#-instalação)
- [⏰ Processamento Agendado (GitHub Actions)](#-processamento-agendado-github-actions)

</br>

## 📓 Sobre

O dashboard integrado ao aplicativo (Área Restrita) apresenta insights sobre as avaliações atribuídas ao grupo durante o dia **06/11 - ExpoTech**. A visão foi criada na versão gratuita do Power BI e contempla:

- Conexão com o banco de dados PostgreSQL via **DirectQuery**;
- Recebimento de dados da **requisição automática via API**;
- Atualização automática via **GitHub Actions**;
- Agendamento de atualização (Power BI Pro teste gratuito) em 8 horários: `12h, 13h, 14h, 15h, 16h, 17h, 18h, 20h`.

</br>

## 🚀 Tecnologias

As principais tecnologias e bibliotecas utilizadas neste projeto são:

* **Python 3.11**
* **SQLAlchemy**
* **PostgreSQL (psycopg2)**
* **UPSERT logic**
* **pandas**
* **requests**
* **Python**

</br>

## ✨ Funcionalidades

Requisições POST para url_endpoint_login, obtendo o **access_token** a partir do usuário e senha, autenticando o acesso aos dados protegidos pela API.


Requisições GET para buscar **reviews/grades** da API.


Conversão da lista de dicionários para **DataFrame** grades_df utilizando **pandas**.


Carregamento de dados no banco de dados utilizando a lógica **UPSERT**.

</br>

## ⚙️ Instalação

É necessário ter o Python (versão 3.10+), Docker e acesso e credenciais para as instâncias de PostgreSQL.

```bash
# clonar o repositório
git clone [https://github.com/Systems-Kronos/kronos-bi.git](https://github.com/Systems-Kronos/kronos-bi.git)

# entrar no diretório
cd kronos-bi

# instalar dependências
pip install -r requirements.txt
````

**Configuração do Ambiente (CDC):**

Crie um arquivo `.env` na raiz do projeto com as variáveis de ambiente para os bancos:

```
SENHA_REQUISICAO='password'
URL_LOGIN='https://expo-tech-backend.onrender.com/users/login'
URL_REVIEWS='https://expo-tech-backend.onrender.com/reviews/project/'

DB_USER='user_neon'
DB_CREDENTIAL='password'
DB_HOST='host_address’'
DB_PORT='port'
DB_NAME='dbKronosNotas'
```


## ⏰ Processamento Agendado (GitHub Actions)

O repositório utiliza GitHub Actions para automação:

**1. Sincronização de Bancos (`atualizar_dados.yml`)**

  * **Frequência:** Executa a cada hora (`cron: '*/30 * * * *`) e por dispatch manual.
  * **Ação:** Procura atualizações e caso tenha alguma, insere no banco de dados, refletindo no PowerBI.


## 📄 Licença

Este projeto está licenciado sob a licença MIT — veja o arquivo [LICENSE](https://www.google.com/search?q=LICENSE) para mais detalhes.


## 💻 Autores
   - [Camilla Moreno](https://github.com/CamillaMorenoA)
   - [Júlia Penna](https://github.com/juliaPnMt1304)
   - [Carlos Perrud](https://github.com/CaduPerrudGerminare)


