# Sistema de Evaluación - API REST

Este proyecto implementa una API REST para un sistema de evaluación de estudiantes en Python utilizando Flask.

## Características

- Gestión de estudiantes
- Sistema de preguntas teóricas y prácticas
- Evaluación automática de respuestas
- Almacenamiento de respuestas en JSON
- Interfaz web para estudiantes

## Requisitos

- Python 3.x
- Flask
- Flask-CORS

## Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/draexx/sistema-evaluacion-api.git
```

2. Instala las dependencias:
```bash
pip3 install flask flask-cors
```
3. Ejecuta la aplicación:
```bash
python3 app.py
```
## Uso
- Accede a la interfaz web en
```
http://localhost:8000
```
## Estructura del Proyecto

```
.
├── app.py                # Servidor Flask principal
├── deque.py             # Implementación de estructura de datos Deque
├── init_questions.py    # Inicialización de preguntas
├── index.html           # Interfaz web principal
├── styles.css           # Estilos CSS de la interfaz
├── app.js              # Lógica del frontend en JavaScript
├── students_data.json  # Almacenamiento de respuestas de estudiantes
└── questions_data.json # Base de datos de preguntas
```
