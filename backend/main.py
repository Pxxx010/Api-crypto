from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests
from dotenv import load_dotenv
import os
from deep_translator import GoogleTranslator
from cachetools import TTLCache, cached
from typing import Dict, Optional

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

# Cache para armazenar traduções por 24 horas
translation_cache = TTLCache(maxsize=1000, ttl=86400)

@cached(cache=translation_cache)
def translate_text(text: str) -> str:
    """
    Traduz o texto para português usando o Google Translate via deep-translator
    """
    try:
        translator = GoogleTranslator(source='en', target='pt')
        return translator.translate(text)
    except Exception as e:
        # Se houver erro na tradução, retorna o texto original
        print(f"Erro na tradução: {str(e)}")
        return text

@app.get("/")
async def read_root():
    return {"message": "API de Citações"}

@app.get("/quote")
async def get_quote():
    try:
        # Busca a citação da API
        response = requests.get(
            API_URL,
            headers={"X-Api-Key": API_KEY}
        )
        response.raise_for_status()
        quote_data = response.json()[0]
        
        # Traduz a citação usando a função com cache
        translated_quote = translate_text(quote_data["quote"])
        
        return {
            "quote": translated_quote,
            "author": quote_data["author"],
            "category": quote_data["category"],
            "original_quote": quote_data["quote"]  # Incluindo a citação original
        }
    except requests.RequestException as e:
        raise HTTPException(
            status_code=500,
            detail="Erro ao buscar citação da API externa"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Erro interno do servidor"
        ) 