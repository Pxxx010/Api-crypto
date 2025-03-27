from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

# Configuração do CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, especifique as origens permitidas
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_KEY = os.getenv("API_NINJAS_KEY", "5W/zvX9f4ODD485SDXY9RQ==m6cVw9yI023WelQF")
API_URL = "https://api.api-ninjas.com/v1/quotes"

@app.get("/")
async def read_root():
    return {"message": "API de Citações"}

@app.get("/quote")
async def get_quote():
    try:
        response = requests.get(
            API_URL,
            headers={"X-Api-Key": API_KEY}
        )
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e)) 