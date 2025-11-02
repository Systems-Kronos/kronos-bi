# Atualização de Dados - Kronos

O repositório faz uma **requisição automática à API do terceiro ano (aplicativo ExpoTech 2025)** a cada **30 minutos**, salvando os dados no banco e mantendo a interface do **Power BI** atualizada automaticamente, com agendamento de carregamento de dados.

---

## 📄 Documentação do Power BI

### Avaliação Feira - Visão Geral
O dashboard integrado ao aplicativo (Área Restrita) apresenta insights sobre as avaliações atribuídas ao grupo durante o dia **06/11 - ExpoTech**. A visão foi criada na versão gratuita do Power BI e contempla:

- Conexão com o banco de dados PostgreSQL via **DirectQuery**;
- Recebimento de dados da **requisição automática via API**;
- Atualização automática via **GitHub Actions**;
- Agendamento de atualização (Power BI Pro teste gratuito) em 8 horários: `12h, 13h, 14h, 15h, 16h, 17h, 18h, 20h`.

### 🔹 Fontes de Dados
- **grade_name**: categoria de avaliação do usuário (4 pontos de atenção: apresentação do projeto, apresentação do stand, ideia usada para resolver o problema, solução desenvolvida);
- **review_id**: identifica o usuário que respondeu à pesquisa (`review-uuid-{numero_stand}-{ordem_resposta}`);
- **score**: nota atribuída pelo usuário (1 a 5);
- **weight**: peso da nota por categoria (0.25 cada, média final da avaliação).