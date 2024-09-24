from fastapi import FastAPI, UploadFile, File, HTTPException
from typing import Optional
import openai
from fastapi.responses import JSONResponse
from starlette.status import HTTP_200_OK
import logging
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
import io
import os

load_dotenv('.env.dev')
openai.api_key = os.getenv("OPENAI.API_KEY")

# Tamaño máximo permitido en MB
MAX_AUDIO_SIZE_MB = 5 
MAX_AUDIO_SIZE_BYTES = MAX_AUDIO_SIZE_MB * 1024 * 1024  # Convertido a bytes

app = FastAPI(
    title="Funnelchat",
    description="Convertidor de audio a texto"
)

# Configura CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"hello ✔": "Audio to text converter"}



@app.post("/audio")
async def chat(audio: Optional[UploadFile] = File(...)):
    print("recibiendo el nombre del audio... ", audio.filename)

    if not audio:
        raise HTTPException(status_code=400, detail="Debe proporcionar un archivo de audio")

    # Leemos el contenido del archivo de audio
    audio_content = await audio.read()

    try:
        # Creamos un archivo en memoria usando io.BytesIO para simular un archivo
        audio_file = io.BytesIO(audio_content)
        audio_file.name = audio.filename

        # Convertimos el audio a texto utilizando OpenAI
        response = openai.Audio.transcribe(
            model="whisper-1",
            file=audio_file
        )

        # Preparamos la respuesta con el texto transcrito y el status code
        responde = {
            "text": response['text'],
            "status": HTTP_200_OK
        }

        # Retornamos la respuesta en formato JSON con el status code
        return JSONResponse(content=responde, status_code=HTTP_200_OK)

    except Exception as e:
        logging.error(f"Error durante la transcripción: {e}")
        raise HTTPException(status_code=500, detail="Error en la transcripción del audio.")



handler = Mangum(app, lifespan="off")
