# API Quote

Uma simples API de citações

## 🚀 Sobre o Projeto

Este projeto é uma aplicação full-stack que permite visualizar citações aleatórias. O sistema é composto por um backend em Python (FastAPI) e um frontend em React/Vite.

## 🛠️ Tecnologias Utilizadas

### Backend
- Python
- FastAPI
- Requests
- python-dotenv
- googletrans

### Frontend
- React
- Vite
- JavaScript/TypeScript

## 📋 Pré-requisitos

- Python 3.x
- Node.js
- npm ou yarn

## 🔧 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/Pxxx010/Api-quote
```

2. Instale as dependências do backend:
```bash
cd backend
pip install -r requirements.txt
```

3. Instale as dependências do frontend:
```bash
cd ../frontend
npm install
```

## 🚀 Como Executar

1. Inicie o backend:
```bash
cd backend
uvicorn main:app --reload
```

2. Em outro terminal, inicie o frontend:
```bash
cd frontend
npm run dev
```

## 📝 Endpoints da API

- `GET /`: Mensagem de boas-vindas
- `GET /quote`: Retorna uma citação traduzida

## 📄 Licença

Este projeto está sob a licença ISC. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
