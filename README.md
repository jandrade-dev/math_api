Aqui está o README atualizado diretamente na conversa:

# Math API

API RESTful desenvolvida com **FastAPI** para realizar operações matemáticas básicas, como soma e média de listas de inteiros.

## 📂 Estrutura do Projeto

```!whitespace-pre
MATH_API/
│-- app/
│ ├── api/
│ │ ├── main.py # Definição das rotas FastAPI
│ ├── library/
│ │ ├── models.py # Classes para operações matemáticas
│ ├── services/
│ │ ├── services.py # Lógica de negócios conectando a API aos modelos
│ ├── tests/
│ │ ├── test_models.py # Testes unitários dos modelos
│ │ ├── test_services.py # Testes unitários dos serviços
│-- requirements.txt # Dependências do projeto
│-- README.md # Documentação do projeto
```

## 🚀 Como Executar o Projeto

### 1️⃣ Clonar o repositório

```!whitespace-pre bash
git clone https://github.com/jandrade-dev/math_api.git
cd math_api
```

### 2️⃣ Criar e ativar um ambiente virtual (opcional, mas recomendado)

```!whitespace-pre bash
python -m venv venv
# Ativar no Windows
venv\Scripts\activate
# Ativar no Linux/Mac
source venv/bin/activate
```

### 3️⃣ Instalar as dependências

```!whitespace-pre bash
pip install -r requirements.txt
```

### 4️⃣ Executar a API

```!whitespace-pre bash
uvicorn app.api.main:app --reload
```

A API estará disponível em **[](http://127.0.0.1:8000)** .

## 📌 Endpoints Disponíveis

### ➤ **Soma de uma lista de números**

```!whitespace-pre http
POST /sum
```
✅ Exemplo de Requisição:
```!whitespace-pre json
{
"numbers": [1, 2, 3, 4]
}
```
🔄 Resposta:
```!whitespace-pre json
{
"result": 10
}
```

### ➤ **Cálculo da média de uma lista de números**

```!whitespace-pre http
POST /average
```
✅ Exemplo de Requisição:
```!whitespace-pre json
{
"numbers": [2, 4, 6, 8]
}
```
🔄 Resposta:
```!whitespace-pre json
{
"result": 5.0
}
```

## 🧪 Como Rodar os Testes

Para executar os testes unitários, utilize o comando:

```!whitespace-pre bash
pytest app/tests
```

## 🛠 Tecnologias Utilizadas

- **Python 3.x**
- **FastAPI**
- **Pytest**
- **Uvicorn**

## 📜 Licença

Este projeto está sob a licença **MIT** . Sinta-se livre para usar e modificar! 🎯