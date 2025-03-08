# Convertidor de Audio a Texto con Inteligencia Artificial

## 📝 Descripción

Este proyecto es una API desarrollada con FastAPI que permite convertir archivos de audio a texto utilizando el modelo Whisper de OpenAI. Esta herramienta es ideal para transcripciones automáticas de grabaciones, notas de voz, entrevistas o cualquier contenido de audio que necesites transformar en texto.

## ✨ Características

- 🔄 Conversión de audio a texto con alta precisión
- 🚀 API rápida y eficiente con FastAPI
- 🌍 Soporte CORS para integraciones con aplicaciones web
- 🔒 Manejo seguro de archivos de audio
- ☁️ Compatible con despliegue serverless (AWS Lambda)

## 🧰 Tecnologías Utilizadas

- **FastAPI**: Framework web de alto rendimiento
- **OpenAI Whisper**: Modelo avanzado de reconocimiento de voz
- **Mangum**: Adaptador para facilitar el despliegue en AWS Lambda
- **Python-dotenv**: Gestión de variables de entorno
- **CORS Middleware**: Para permitir solicitudes de diferentes orígenes

## 📋 Requisitos Previos

- Python 3.8 o superior
- Cuenta en OpenAI con API Key
- Pip (gestor de paquetes de Python)

## 🚀 Instalación

1. **Clonar el repositorio**

```bash
git clone https://github.com/tu-usuario/convertidor-audio-texto.git
cd convertidor-audio-texto
```

2. **Crear un entorno virtual**

```bash
python -m venv venv
```

3. **Activar el entorno virtual**

En Windows:
```bash
venv\Scripts\activate
```

En macOS/Linux:
```bash
source venv/bin/activate
```

4. **Instalar dependencias**

```bash
pip install -r requirements.txt
```

5. **Configurar variables de entorno**

Crea un archivo `.env.dev` en la raíz del proyecto con el siguiente contenido:

```
OPENAI.API_KEY=tu_api_key_de_openai
```

## 🔧 Uso

### Iniciar el servidor localmente

```bash
uvicorn main:app --reload
```

El servidor estará disponible en `http://localhost:8000`

### Endpoints

#### GET /

Endpoint de prueba para verificar que el servicio está funcionando.

**Respuesta**:
```json
{
  "hello ✔": "Audio to text converter"
}
```

#### POST /audio

Convierte un archivo de audio a texto.

**Parámetros**:
- `audio`: Archivo de audio (máximo 5MB)

**Ejemplo de solicitud usando curl**:
```bash
curl -X POST "http://localhost:8000/audio" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "audio=@tu_archivo_audio.mp3"
```

**Respuesta exitosa**:
```json
{
  "text": "Texto transcrito del audio...",
  "status": 200
}
```

### Documentación de la API

FastAPI genera automáticamente la documentación de la API. Puedes acceder a:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 🔍 Limitaciones

- Tamaño máximo de archivo de audio: 5MB
- Formatos de audio soportados: MP3, M4A, WAV, MPG, MPEG, WEBM

## 🚀 Despliegue

Este proyecto está diseñado para ser desplegado fácilmente en AWS Lambda gracias a Mangum.

### Pasos para el despliegue en AWS Lambda

1. **Empaquetar la aplicación**
   Asegúrate de incluir todas las dependencias en tu paquete de despliegue.

2. **Configurar un API Gateway**
   Configura un API Gateway en AWS para exponer tu función Lambda.

3. **Configurar variables de entorno**
   Define la variable `OPENAI.API_KEY` en la configuración de AWS Lambda.

4. **Definir el handler**
   En la configuración de AWS Lambda, establece el handler como `main.handler`.

## 🧪 Testing

Para ejecutar las pruebas (si están disponibles):

```bash
pytest
```

## 🛠️ Estructura del Proyecto

```
convertidor-audio-texto/
├── main.py            # Archivo principal con la API
├── requirements.txt   # Dependencias del proyecto
├── .env.dev           # Variables de entorno para desarrollo
└── README.md          # Documentación
```

## 📖 Explicación del Código

### Configuración Inicial

```python
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

# Carga las variables de entorno del archivo .env.dev
load_dotenv('.env.dev')

# Configura la API key de OpenAI
openai.api_key = os.getenv("OPENAI.API_KEY")
```

### Límites de Tamaño

```python
# Tamaño máximo permitido en MB
MAX_AUDIO_SIZE_MB = 5 
MAX_AUDIO_SIZE_BYTES = MAX_AUDIO_SIZE_MB * 1024 * 1024  # Convertido a bytes
```

### Creación de la Aplicación

```python
app = FastAPI(
    title="Convertidor de Audio a Texto",
    description="API para convertir audio a texto"
)

# Configura CORS para permitir solicitudes desde cualquier origen
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### Endpoints

```python
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
```

### Configuración para AWS Lambda

```python
handler = Mangum(app, lifespan="off")
```

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, sigue estos pasos:

1. Haz un fork del repositorio
2. Crea una rama para tu función (`git checkout -b feature/nueva-funcionalidad`)
3. Haz commit de tus cambios (`git commit -m 'Añade nueva funcionalidad'`)
4. Sube la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

## 📞 Contacto

Para cualquier consulta o sugerencia, puedes contactarme a través de:

- GitHub: [tu-usuario](https://github.com/tu-usuario)
- Email: tu-email@ejemplo.com

---

Desarrollado con ❤️ usando FastAPI y OpenAI Whisper
