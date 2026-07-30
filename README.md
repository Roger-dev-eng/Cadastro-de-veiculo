# Cadastro de Veículos - Pipeline de Dados FIPE

## Conteúdo
- [Descrição](#descrição)
- [Objetivo](#objetivo)
- [Estrutura do projeto](#estrutura-do-projeto)
- [Explicação dos principais componentes](#explicação-dos-principais-componentes)
- [Como executar localmente](#como-executar-localmente)
- [Como executar com Docker](#como-executar-com-docker)
- [Deploy no Render com Supabase](#deploy-no-render-com-supabase)
- [Resultados e análises](#resultados-e-análises)
- [O que foi aprendido](#o-que-foi-aprendido)
- [Tecnologias utilizadas](#tecnologias-utilizadas)


## Descrição

Este projeto implementa uma **pipeline de dados automatizada** que coleta informações da API FIPE, transforma os dados e os disponibiliza em um dashboard interativo. Os registros de veículos — marca, modelo, ano, combustível e preço — são persistidos em PostgreSQL. O projeto usa **Python**, **SQLAlchemy** e **Streamlit**. No desenvolvimento local, o PostgreSQL é executado com Docker Compose; em produção, a aplicação é publicada no **Render** e se conecta a um banco PostgreSQL hospedado no **Supabase**.

Para acessar a aplicação: https://pipeline-de-dados-fipe.onrender.com/

## Objetivo

- Automatizar a coleta de dados da API FIPE (Parallelum).
- Limpar, validar e padronizar os dados coletados.
- Armazenar os registros em PostgreSQL, localmente ou no Supabase em produção.
- Evitar duplicidades por código FIPE, ano-modelo e combustível.
- Disponibilizar análises visuais de preços, marcas, anos e combustíveis.
- Documentar uma implantação segura no Render usando variáveis de ambiente.

## Estrutura do Projeto

```
cadastro-veiculos/
│
├── app/
│   ├── __init__.py
│   ├── db/
│   │   ├── __init__.py
│   │   └── engine.py         # Inicializa a conexão com o PostgreSQL
│   ├── dashboard/
│   │   ├── __init__.py
│   │   ├── charts.py         # Gráficos interativos do dashboard
│   │   ├── dashboard.py      # Interface Streamlit
│   │   └── queries.py        # Consultas ao banco para o dashboard
│   ├── pipeline/
│   │   ├── __init__.py
│   │   └── fipe_import.py    # Pipeline de coleta e inserção de dados da API FIPE
│   └── utils/
│       ├── __init__.py
│       └── funcoes.py        # Funções de limpeza, validação e logs
│
├── logs/                     # Armazena logs e cache
│
├── run.py                    # Executa toda a pipeline
│
├── requirements.txt
│
├── .env                      # Configuração local das variáveis de ambiente
│
└── README.md
```


---


## Explicação dos principais componentes

#### `app/pipeline/fipe_import.py`
Responsável por:
- Coletar dados da **API FIPE**.
- Tratar os dados, incluindo limpeza de valores monetários e validação de anos.
- Evitar duplicidade ao inserir no banco.
- Criar a tabela `fipe_carros` caso não exista.
- Inserir os dados tratados no banco PostgreSQL.


#### `app/dashboard/dashboard.py`
Interface web em **Streamlit** com:
- Painel visual para executar a coleta FIPE sem depender do terminal.
- Acompanhamento de progresso, etapa atual, marcas processadas, registros coletados e batches gravados.
- Resumo final com registros coletados, válidos, novos inseridos e já existentes.
- Filtros por marca, combustível e ano.
- Indicadores de volume, marcas, preço médio e maior preço.
- Gráficos interativos com **Plotly**.
- Tabela dos registros filtrados.


#### `run.py`
Inicia o dashboard Streamlit, que já permite executar a coleta FIPE e acompanhar os dados no navegador.


---

## Como executar localmente

Instale as dependências:

```bash
pip install -r requirements.txt
```

Configure as variáveis necessárias do banco de dados no arquivo `.env`.

O `.env` deve conter as variáveis usadas pelo PostgreSQL:

```env
POSTGRES_DB=nome_do_banco
POSTGRES_USER=usuario_do_banco
POSTGRES_PASSWORD=sua_senha_local
DATABASE_URL=postgresql+psycopg2://usuario_do_banco:sua_senha_local@localhost:5432/nome_do_banco
```

Variáveis opcionais de configuração:

```env
RECORDS_LIMIT=650       # Limite de registros coletados (padrão: 600)
FIPE_TIMEOUT=10         # Timeout em segundos para requisições à API
FIPE_SLEEP_TIME=0.3     # Pausa entre requisições (reserva para uso futuro)

Depois inicie o projeto da seguinte forma:
```bash
python run.py
```

## Como executar com Docker

O projeto pode ser executado com Docker Compose usando o arquivo `.env` atual.

O `.env` deve conter as variáveis:

```env
POSTGRES_DB=nome_do_banco
POSTGRES_USER=usuario_do_banco
POSTGRES_PASSWORD=sua_senha_local
```

Para uso local fora do Docker, mantenha também a `DATABASE_URL` apontando para `localhost`:

Variáveis opcionais de configuração:

```env
RECORDS_LIMIT=650       # Limite de registros coletados (padrão: 600)
FIPE_TIMEOUT=10         # Timeout em segundos para requisições à API
FIPE_SLEEP_TIME=0.3     # Pausa entre requisições (reserva para uso futuro)
```

Dentro do Docker, o `docker-compose.yml` monta a `DATABASE_URL` automaticamente usando o host interno `db`.

Com o Docker Desktop aberto, execute:

```bash
docker compose up --build
```

Depois acesse:

```text
http://localhost:8501
```

## Deploy no Render com Supabase

Durante o desenvolvimento, o PostgreSQL foi executado localmente com Docker
Compose. Esse ambiente permitiu testar a pipeline e o dashboard de forma
isolada, usando a mesma variavel `DATABASE_URL` adotada em producao.

Na publicacao, a aplicacao foi configurada como um Web Service Docker no
Render. O `Dockerfile` inicia o Streamlit em `0.0.0.0` e usa a porta informada
pelo Render por meio da variavel `PORT`.

O banco de dados de producao foi hospedado no [Supabase]. Ao executar a coleta no dashboard publicado, a pipeline cria a
tabela `fipe_carros` quando necessario e grava os registros diretamente no
banco hospedado no Supabase.

## Resultados e Análises

### Visão Geral

Após a execução da pipeline, os dados extraídos da API FIPE são processados, armazenados e analisados, gerando insights valiosos sobre o mercado automotivo brasileiro.


Os dados são persistidos na tabela **`fipe_carros`** do PostgreSQL, contendo informações completas sobre:
- Marcas e modelos de veículos
- Preços de referência FIPE
- Anos de fabricação
- Tipos de combustível
- Códigos FIPE

## O que foi aprendido

O desenvolvimento deste projeto consolidou conhecimentos práticos sobre:

- Construção de uma pipeline ETL, desde o consumo de uma API pública até a persistência dos dados.
- Tratamento e validação de dados com Pandas antes da gravação no banco.
- Uso de restrições de unicidade e `ON CONFLICT` no PostgreSQL para evitar registros duplicados.
- Criação de um dashboard interativo com Streamlit e Plotly para explorar os dados coletados.
- Containerização da aplicação e do banco local com Docker e Docker Compose.
- Separação entre ambientes local e de produção com variáveis de ambiente.
- Publicação de uma aplicação Python no Render e integração com o PostgreSQL gerenciado pelo Supabase.

## Tecnologias Utilizadas


| Tecnologia    | Versão  | Função                                    |
|---------------|---------|-------------------------------------------|
| **Python**    | 3.13    | Linguagem principal do projeto            |
| **PostgreSQL**| 16      | Banco de dados relacional                 |
| **Supabase**  | -       | PostgreSQL gerenciado no ambiente de produção |
| **SQLAlchemy**| 2.0+    | ORM para mapeamento objeto-relacional     |
| **Pandas**    | 2.1+    | Manipulação e análise de dados            |
| **Requests**  | 2.31+   | Cliente HTTP para consumo da API FIPE     |
| **Matplotlib**  | 3.8+    | Criação de gráficos estáticos          |
| **Seaborn**     | 0.13+   | Visualizações estatísticas avançadas   |
| **Streamlit**   | 1.57+   | Interface web e dashboard interativo   |
| **Plotly**      | 6.7+    | Gráficos interativos                   |
| **python-dotenv**| 1.0+    | Gerenciamento de variáveis de ambiente |
| **psycopg2-binary** | 2.9+ | Driver PostgreSQL para Python          |
| **Docker**    | -       | Containerização da aplicação             |
| **Docker Compose** | -   | Orquestração do ambiente local           |
| **Render**    | -       | Hospedagem e deploy da aplicação         |
---
