import json

questions_db = {
    "theoretical": [
        {
            "id": "1a",
            "question": "¿Qué es un TAD (Tipo Abstracto de Datos) y cuál es su importancia en la programación?",
            "points": 5,
            "type": "text",
            "answer_key": ["tipo abstracto", "datos", "encapsulamiento", "interfaz", "implementación"]
        },
        # ... resto de las preguntas teóricas ...
    ],
    "problem_solving": [
        # ... preguntas de resolución de problemas ...
    ],
    "programming": [
        # ... preguntas de programación ...
    ]
}

# Guardar las preguntas en un archivo JSON
with open('questions_data.json', 'w') as f:
    json.dump(questions_db, f, indent=4)