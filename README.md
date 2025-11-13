# Cadastro de Veículos - Pipeline de Dados FIPE

## Descrição

Este projeto implementa uma **pipeline de dados automatizada** para coletar, armazenar e analisar informações da **tabela FIPE**, que contém dados de veículos (marca, modelo, ano, combustível e preço).  
O objetivo é demonstrar o processo completo de **extração, transformação e carregamento (ETL)** de dados de uma API pública até um banco de dados relacional, com visualizações analíticas para insights.

A pipeline foi construída em **Python**, utilizando **PostgreSQL** como banco de dados e diversas bibliotecas para manipulação e visualização dos dados.

## Objetivo

-  Automatizar a **coleta de dados** da API FIPE (Parallelum).
- Fazer a **limpeza e padronização** dos dados coletados.
- Armazenar os dados tratados em um **banco PostgreSQL**.
- Evitar inserções duplicadas no banco.
- Gerar **análises estatísticas e visuais** sobre os preços médios por marca e tipo de combustível.

## Estrutura do Projeto

```
cadastro-veiculos/
│
├──  app/
│   ├── __init__.py           # Inicializa a conexão com o banco PostgreSQL
│   ├── fipe_import.py        # Pipeline de coleta e inserção de dados da API FIPE
│   ├── analysis.py           # Funções de análise e consultas SQL
│   └── utils/
│         ├── __init__.py     # Permite importar funções de utilidade
│         ├── helpers.py      # Tem funções de limpeza, validação e logs
│
├──  CRUD/                    # Permite a criação de uma banco de dados para cadastrar, listar, atualizar e remover carros.
│     └── cadastro.py
│   ├── __init__.py
│   ├── connection.py         # Pool de conexões PostgreSQL
│   ├── schemas.py            # Definição de tabelas (DDL)
│   ├── repository.py         # Operações CRUD
│   └── migrations/
│       ├── 001_initial_schema.sql
│       └── 002_add_indexes.sql
│
├──  domain/
│   ├── __init__.py
│   ├── entities.py  # Classes de domínio (Vehicle, Brand, Model)
│   └── value_objects.py   # Objetos de valor (Price, Year, FuelType)
│
├──  api/
│   ├── __init__.py
│   ├── fipe_client.py                # Cliente HTTP para API FIPE
│   └── rate_limiter.py               # Controle de taxa de requisições
│
├──  analytics/
│   ├── __init__.py
│   ├── reports.py                    # Geração de relatórios
│   ├── metrics.py                    # Cálculo de métricas e KPIs
│   └── visualizations.py             # Gráficos e dashboards
│
├──  shared/
│   ├── __init__.py
│   ├── config.py                     # Configurações globais (env vars)
│   ├── logger.py                     # Sistema de logs centralizado
│   ├── exceptions.py                 # Exceções customizadas
│   └── validators.py                 # Validadores reutilizáveis
│
├──  cli/
│   ├── __init__.py
│   └── commands.py                   # Interface de linha de comando
│
├── 📓 notebooks/
│   └── exploratory_analysis.ipynb    # Análises exploratórias
│
├──  storage/
│   ├── cache/                        # Cache de requisições HTTP
│   ├── exports/                      # Arquivos CSV, JSON exportados
│   └── logs/                         # Arquivos de log rotativos
│
├──  deployment/
│   ├── docker/
│   │   ├── Dockerfile
│   │   └── docker-compose.yml
│   └── kubernetes/
│       └── deployment.yaml
│
├──  tests/
│   ├── unit/                         # Testes unitários
│   ├── integration/                  # Testes de integração
│   └── fixtures/                     # Dados de teste
│
├── main.py                           # 🎬 Ponto de entrada principal
├── pyproject.toml                    # Configuração do projeto (PEP 517/518)
├── .env.template                     # Template de variáveis de ambiente
├── .dockerignore
├── .gitignore
└── README.md
```

---

## 📋 Descrição dos Módulos

### 📦 **pipeline/**
Contém toda a lógica do processo ETL:
- **extract.py**: Busca dados da API FIPE
- **transform.py**: Limpa, normaliza e valida os dados
- **load.py**: Insere dados no PostgreSQL
- **orchestrator.py**: Coordena a execução das etapas

### 🗄️ **database/**
Gerenciamento completo do banco de dados:
- **connection.py**: Pool de conexões otimizado
- **schemas.py**: Definições de tabelas e índices
- **repository.py**: Padrão Repository para operações de dados
- **migrations/**: Scripts SQL versionados

### 🎯 **domain/**
Camada de domínio do negócio:
- **entities.py**: Entidades principais (Veículo, Marca, Modelo)
- **value_objects.py**: Objetos imutáveis (Preço, Ano, Tipo de Combustível)

### 🌐 **api/**
Comunicação com APIs externas:
- **fipe_client.py**: Cliente HTTP com retry e timeout
- **rate_limiter.py**: Controle de requisições por segundo

### 📊 **analytics/**
Análises e visualizações:
- **reports.py**: Relatórios automatizados
- **metrics.py**: KPIs e estatísticas
- **visualizations.py**: Gráficos interativos

### 🔧 **shared/**
Utilitários compartilhados:
- **config.py**: Carrega variáveis de ambiente
- **logger.py**: Logs estruturados (JSON)
- **exceptions.py**: Hierarquia de exceções
- **validators.py**: Validações de CPF, CNPJ, placas, etc.

### 💻 **cli/**
Interface de linha de comando:
```bash
python -m cli run-pipeline
python -m cli export-data --format csv
python -m cli generate-report
```

### 💾 **storage/**
Armazenamento local:
- **cache/**: Cache de respostas HTTP (Redis-like)
- **exports/**: Dados exportados em vários formatos
- **logs/**: Histórico de execuções

### 🚀 **deployment/**
Configurações de deploy:
- **Docker**: Containerização da aplicação
- **Kubernetes**: Orquestração em produção

### 🧪 **tests/**
Testes automatizados:
- **unit/**: Testes isolados de funções
- **integration/**: Testes de integração com banco
- **fixtures/**: Dados mock para testes

---

## 🚀 Como Usar
```bash
# Instalar dependências
pip install -e .

# Configurar ambiente
cp .env.template .env

# Executar pipeline completo
python main.py

# Usar CLI
python -m cli run-pipeline --source fipe
python -m cli generate-report --period monthly
```

---

## 📦 Dependências Principais

- **PostgreSQL**: Banco de dados relacional
- **psycopg2**: Driver Python para PostgreSQL
- **requests**: Cliente HTTP
- **pandas**: Manipulação de dados
- **click/typer**: Interface CLI
- **python-dotenv**: Gerenciamento de variáveis de ambiente
- **loguru**: Sistema de logs avançado

---

## 🔄 Fluxo de Dados
```
API FIPE → Extract → Transform → Validate → Load → PostgreSQL
                                                         ↓
                                                    Analytics
```

---

## 📝 Convenções

- **Código**: PEP 8 (Black formatter)
- **Commits**: Conventional Commits
- **Branches**: GitFlow
- **Testes**: Cobertura mínima de 80%