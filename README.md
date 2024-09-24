# 🎧 Funnelchat: Audio to Text Converter API

## 📋 Descripción
**Funnelchat Audio to Text Converter** es un servicio basado en FastAPI que convierte archivos de audio en texto utilizando el modelo **Whisper** de OpenAI. Permite subir archivos de audio y obtener la transcripción en formato JSON. Además, está listo para integrarse en proyectos frontend con soporte CORS para solicitudes desde cualquier origen.

## 🚀 Funcionalidades
- 🎙️ **Conversión de Audio a Texto**: Sube un archivo de audio y obtén su transcripción en texto utilizando la IA de OpenAI.
- 🔒 **Soporte CORS**: Permite hacer solicitudes desde cualquier frontend (Angular, React, Vue, etc.).
- 🧑‍💻 **Integración con Postman**: Colección de ejemplos listos para probar con Postman.
- 🔐 **Variables de Entorno**: Las claves de API y configuraciones sensibles se manejan de manera segura mediante archivos de entorno (`.env`).

## 🛠️ Tecnologías Utilizadas
- **FastAPI**: Framework web para crear APIs de alto rendimiento.
- **OpenAI Whisper**: Modelo de IA para la transcripción de audio a texto.
- **Mangum**: Adaptador para implementar en entornos serverless (AWS Lambda, etc.).
- **Uvicorn**: Servidor ASGI rápido y liviano para ejecutar la API.
- **Dotenv**: Manejo de variables de entorno para configuración segura.

## 📡 Endpoints

### 1. 🌐 Root (`/`)
**Método**: `GET`  
**Descripción**: Punto de control de estado. Útil para verificar que el servicio está en funcionamiento.  
**Respuesta**:
```json
{
    "hello ✔": "Audio to text converter"
}
# 🎧 Funnelchat: Audio to Text Converter API

## 📋 Descripción
**Funnelchat Audio to Text Converter** es un servicio basado en FastAPI que convierte archivos de audio en texto utilizando el modelo **Whisper** de OpenAI. Permite subir archivos de audio y obtener la transcripción en formato JSON. Además, está listo para integrarse en proyectos frontend con soporte CORS para solicitudes desde cualquier origen.

## 🚀 Funcionalidades
- 🎙️ **Conversión de Audio a Texto**: Sube un archivo de audio y obtén su transcripción en texto utilizando la IA de OpenAI.
- 🔒 **Soporte CORS**: Permite hacer solicitudes desde cualquier frontend (Angular, React, Vue, etc.).
- 🧑‍💻 **Integración con Postman**: Colección de ejemplos listos para probar con Postman.
- 🔐 **Variables de Entorno**: Las claves de API y configuraciones sensibles se manejan de manera segura mediante archivos de entorno (`.env`).

## 🛠️ Tecnologías Utilizadas
- **FastAPI**: Framework web para crear APIs de alto rendimiento.
- **OpenAI Whisper**: Modelo de IA para la transcripción de audio a texto.
- **Mangum**: Adaptador para implementar en entornos serverless (AWS Lambda, etc.).
- **Uvicorn**: Servidor ASGI rápido y liviano para ejecutar la API.
- **Dotenv**: Manejo de variables de entorno para configuración segura.

## 📡 Endpoints

### 1. 🌐 Root (`/`)
**Método**: `GET`  
**Descripción**: Punto de control de estado. Útil para verificar que el servicio está en funcionamiento.  
**Respuesta**:
```json
{
    "hello ✔": "Audio to text converter"
}
```

### 2. 🎤 Audio (/audio)
Método: POST
**Descripción: Sube un archivo de audio y recibe la transcripción del contenido en texto.
Parámetros:

audio (archivo): El archivo de audio a transcribir. El tamaño máximo permitido es de 5MB.

```
curl -X POST "http://127.0.0.1:8000/audio" -F "audio=@ruta/al/audio.ogg"

Ejemplo de solicitud usando form-data en Postman:

Selecciona el método POST.
En el cuerpo de la solicitud, elige la opción form-data.
Agrega una clave llamada audio y selecciona el archivo de audio en el campo de valor.
Envía la solicitud.

```

Respuesta:
```json

{
    "text": "Texto transcrito del archivo de audio.",
    "status": 200
}
```

Respuesta en caso de error:

```json
{
    "detail": "Debe proporcionar un archivo de audio."
}
```


### 📦 Instalación y Configuración
## 📋 Requisitos:
- Python 3.8+
- FastAPI
- OpenAI API Key


## OPENAI_API_KEY=tu_clave_de_openai

### 🔧 Dependencias

- fastapi==0.99.0
- mangum==0.14.0
- uvicorn==0.23.0
- openai==0.28.0
- lxml==4.9.0
- python-dotenv==1.0.1
- python-multipart==0.0.9