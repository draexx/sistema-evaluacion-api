# Sistema de Evaluación - API REST

Este proyecto implementa una API REST para un sistema de evaluación de estudiantes en Python utilizando Flask.

## Características

- Gestión de estudiantes
- Sistema de preguntas teóricas y prácticas
- Evaluación automática de respuestas
- Almacenamiento de respuestas en JSON
- Interfaz web para estudiantes
- Documentación interactiva con Swagger

## Requisitos

- Python 3.x
- Flask
- Flask-CORS
- Flasgger (para documentación Swagger)

## Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/draexx/sistema-evaluacion-api.git
```

2. Instala las dependencias:
```bash
pip3 install flask flask-cors flasgger
```
3. Inicializa la base de datos de preguntas:
```bash
python3 init_questions.py
```
## Ejecución del Sistema
### Backend (API REST)
1. Ejecuta el servidor Flask:
```bash
python3 app.py
```
El servidor API estará disponible en:
- API: http://127.0.0.1:5000
- Documentación Swagger: http://127.0.0.1:5000/docs
### Frontend (Interfaz Web)
1. En otra terminal, inicia un servidor web simple para el frontend:
```bash
python3 -m http.server 8000
```
2. Accede a la interfaz web en tu navegador:
```
http://localhost:8000
```
## Estructura del Proyecto

```
.
├── app.py               # Servidor Flask principal
├── deque.py             # Implementación de estructura de datos Deque
├── init_questions.py    # Inicialización de preguntas
├── index.html           # Interfaz web principal
├── styles.css           # Estilos CSS de la interfaz
├── app.js               # Lógica del frontend en JavaScript
├── students_data.json   # Almacenamiento de respuestas de estudiantes
└── questions_data.json # Base de datos de preguntas
```
## Documentación de la API

La API está documentada usando Swagger/OpenAPI. Para acceder a la documentación:

1. Inicia el servidor Flask:
```bash
python3 app.py
```
2. Accede a la documentación en tu navegador:
```
http://127.0.0.1:5000/docs
```

### La documentación incluye:

- Descripción detallada de cada endpoint
- Esquemas de request/response
- Ejemplos de uso
- Interfaz interactiva para probar la API

### Beneficios de usar Swagger:
- Documentación interactiva
- Posibilidad de probar los endpoints directamente
- Documentación siempre actualizada
- Generación automática de clientes
- Facilita el entendimiento de la API para otros desarrolladores

### Endpoints Principales
- GET /students : Obtiene la lista de estudiantes registrados
- POST /submit : Envía respuestas de estudiantes
- GET /grade/<student_id> : Obtiene la calificación de un estudiante
- GET /questions : Obtiene la lista de preguntas disponibles
## Evaluación
El sistema incluye diferentes tipos de preguntas:
- Preguntas teóricas (evaluación por palabras clave)
- Problemas de resolución (evaluación manual/automática)
- Ejercicios de programación (evaluación automática)

## Estructura de Datos JSON
### Estructura del Archivo questions_data.json
```json
{
    "theoretical": [
        {
            "id": "1a",
            "question": "¿Qué es un TAD?",
            "points": 5,
            "type": "text",
            "answer_key": ["palabra1", "palabra2"]
        }
    ],
    "problem_solving": [
        {
            "id": "3",
            "question": "Resolver problema X",
            "points": 15,
            "type": "text",
            "answer_key": ["respuesta1", "respuesta2"]
        }
    ],
    "programming": [
        {
            "id": "5",
            "question": "Implementar deque",
            "points": 25,
            "type": "code",
            "test_cases": [
                {
                    "setup": "código inicial",
                    "operations": ["operación1", "operación2"],
                    "expected": {"result": "valor esperado"}
                }
            ]
        }
    ]
}
```
### Estructura del Archivo students_data.json
```json
{
    "student_id": {
        "question_id": {
            "answer": "respuesta del estudiante",
            "timestamp": 1234567890,
            "graded": false,
            "score": 0
        }
    }
}
```
### Control de Versiones
Los archivos JSON están excluidos del control de versiones por seguridad y privacidad. Sin embargo, se proporciona una estructura de ejemplo para referencia. Para inicializar el sistema:

1. Crea questions_data.json usando el script:
```bash
python3 init_questions.py
```
2. El archivo students_data.json se creará automáticamente al recibir las primeras respuestas.

## Seguridad
- Los archivos JSON están incluidos en .gitignore para proteger los datos
- Validación de estudiantes registrados
- Control de acceso a las calificaciones
- Mantener copias de seguridad locales de los datos
- Usar los ejemplos proporcionados como plantilla
### Notas Importantes
- El backend (Flask) debe estar corriendo en el puerto 5000
- El frontend debe estar corriendo en el puerto 8000
- Usa 127.0.0.1 en lugar de localhost para evitar problemas de CORS
- Asegúrate de que ambos servidores estén ejecutándose simultáneamente
## Contribución
1. Haz fork del repositorio
2. Crea una rama para tu feature ( git checkout -b feature/nueva-caracteristica )
3. Realiza tus cambios y haz commit ( git commit -am 'Agrega nueva característica' )
4. Push a la rama ( git push origin feature/nueva-caracteristica )
5. Crea un Pull Request