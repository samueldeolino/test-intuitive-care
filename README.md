# Teste Técnico Intuitive Care 🏥

Este projeto implementa uma solução completa para processamento e disponibilização de dados da ANS (Agência Nacional de Saúde Suplementar), oferecendo uma suite integrada de ferramentas para extração, transformação e disponibilização de dados através de uma API REST.

## 📋 Visão Geral

O projeto é dividido em quatro módulos principais, cada um com uma responsabilidade específica no pipeline de dados:

1. **Web Scraping**: Extração automatizada de dados do portal da ANS
2. **Data Transformation**: Processamento e limpeza dos dados extraídos
3. **Database Testing**: Implementação de testes e operações em banco de dados
4. **API REST**: Interface para consulta dos dados processados

## 🏗️ Estrutura do Projeto

### 1. Web Scraping (`/web-scraping`)

Módulo responsável pela extração automática de dados do portal da ANS.

- Utiliza BeautifulSoup4 para parsing HTML
- Download automático de arquivos PDF e CSV
- Tratamento de exceções e retry em caso de falhas
- Logs detalhados do processo de extração

### 2. Data Transformation (`/data-transformation`)

Módulo de processamento e transformação dos dados brutos.

- Conversão de PDFs para formato tabular
- Limpeza e normalização de dados
- Validação de consistência
- Exportação para formatos estruturados (CSV)

### 3. Database Testing (`/database-testing`)

Suite completa de testes e operações com banco de dados.

- Scripts SQL para criação e população de tabelas
- Queries analíticas
- Testes de integridade e consistência
- Índices e otimizações de performance

### 4. API Test (`/api-test`)

API RESTful moderna desenvolvida com FastAPI.

- Documentação automática com Swagger/OpenAPI
- Validação de dados com Pydantic
- Cache de respostas para melhor performance
- Tratamento de erros padronizado

## 🔌 Endpoints da API

### Busca por Razão Social

```http
GET /buscar/{termo}/{ordem}
```

- **Descrição**: Pesquisa operadoras de saúde por termo na razão social
- **Parâmetros**:
  - `termo`: String para busca na razão social
  - `ordem`: Ordenação por data de registro ('crescente'/'decrescente')
- **Exemplo**: `GET /buscar/unimed/crescente`

### Busca por CNPJ

```http
GET /cnpj/{cnpj}
```

- **Descrição**: Retorna dados detalhados de uma operadora por CNPJ
- **Parâmetros**:
  - `cnpj`: CNPJ da operadora (apenas números)
- **Exemplo**: `GET /cnpj/12345678000190`

### Busca por Estado

```http
GET /estado/{uf}
```

- **Descrição**: Lista todas as operadoras de um estado específico
- **Parâmetros**:
  - `uf`: Sigla do estado (2 caracteres)
- **Exemplo**: `GET /estado/SP`

Todos os endpoints retornam respostas no formato JSON com os seguintes campos:

- Razão Social
- Nome Fantasia
- CNPJ
- Data de Registro ANS
- Modalidade
- UF
- Status Operacional

## 🛠️ Pré-requisitos

### Software

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Git

### Bibliotecas Principais

- FastAPI: Framework web moderno e rápido
- Pandas: Manipulação e análise de dados
- BeautifulSoup4: Web scraping
- Tabula-py: Extração de dados de PDFs
- SQLAlchemy: ORM para banco de dados
- Uvicorn: Servidor ASGI de alta performance
- Requests: Consumir dados de APIs web

## 🚀 Instalação e Configuração

### 1. Clone o Repositório

```bash
git clone https://github.com/seu-usuario/test-intuitive-care-main.git
cd test-intuitive-care-main
```

### 2. Configure o Ambiente Virtual

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente (Linux/Mac)
source venv/bin/activate

# Ativar ambiente (Windows)
.\venv\Scripts\activate
```

### 3. Instale as Dependências

```bash
# Atualizar pip
python -m pip install --upgrade pip

# Instalar dependências
pip install -r requirements.txt
```

## 🔧 Execução dos Módulos

### 1. Web Scraping

```bash
# Navegar até o diretório
cd web-scraping/scripts

# Executar o scraper
python main.py
```

### 2. Data Transformation

```bash
# Navegar até o diretório
cd data-transformation

# Executar transformação
python main.py
```

### 3. Database Testing

```bash
# Navegar até o diretório
cd database-testing

# Executar scripts SQL na ordem

financial_statements.sql
active_health_plan_operators.sql
analytical_query.sql
```

### 4. API

```bash
# Navegar até o diretório
cd api-test

# Iniciar a API
uvicorn api:app --reload

# Acessar documentação
open http://localhost:8000/docs
```

## 📝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request
