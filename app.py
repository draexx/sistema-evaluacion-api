from flask import Flask, request, jsonify
from flask_cors import CORS
from flasgger import Swagger, swag_from
import json
import time
import os

app = Flask(__name__)
CORS(app)

# Rutas de archivos JSON
QUESTIONS_FILE = 'questions_data.json'
STUDENTS_FILE = 'students_data.json'

# Lista de estudiantes registrados
registered_students = {
    "1": "ANDERSON TAYLOR SOPHIA MIA",
    "2": "BAKER ADAMS JUSTIN TYLER",
    "3": "CLARK LEWIS CHRISTOPHER RYAN",
    "4": "DAVIS WILSON OLIVIA GRACE",
    "5": "EVANS MARTIN ETHAN LUCAS",
    "6": "FLORES GARCIA ISABELLA AVA",
    "7": "GONZALEZ LOPEZ MASON NOAH",
    "8": "HARRIS MOORE WILLIAM JAMES",
    "9": "JACKSON WHITE EMILY GRACE",
    "10": "KING WRIGHT DANIEL JOSEPH",
    "11": "LEWIS YOUNG VICTORIA ROSE",
    "12": "MARTINEZ BROWN ELIZABETH ANN",
    "13": "NELSON HILL RACHEL LAUREN",
    "14": "PARKER RODRIGUEZ ANDREW THOMAS",
    "15": "QUINN THOMPSON MADISON CLAIRE",
    "16": "ROBINSON WALKER JOSHUA DAVID",
    "17": "SMITH JOHNSON MICHAEL JAMES",
    "18": "THOMAS MILLER ASHLEY NICOLE",
    "19": "WILLIAMS HALL ALEXANDER DAVID",
    "20": "YOUNG ALLEN EMMA SOPHIA"
}

def load_questions():
    """Carga las preguntas desde el archivo JSON"""
    if os.path.exists(QUESTIONS_FILE):
        with open(QUESTIONS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_data(data, filename):
    """Guarda datos en un archivo JSON"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

# Cargar preguntas al inicio
questions_db = load_questions()

# Base de datos en memoria para las respuestas de los estudiantes
students_db = {}

# Configuración de Swagger
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'apispec',
            "route": '/apispec.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/docs"
}

swagger = Swagger(app, config=swagger_config)

@app.route('/students', methods=['GET'])
@swag_from({
    'responses': {
        200: {
            'description': 'Lista de estudiantes registrados',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'string'},
                    'name': {'type': 'string'}
                }
            }
        }
    }
})
def get_students():
    """
    Endpoint para obtener la lista de estudiantes
    ---
    tags:
      - students
    responses:
      200:
        description: Lista de estudiantes registrados
    """
    return jsonify(registered_students)

@app.route('/submit', methods=['POST'])
@swag_from({
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'student_id': {'type': 'string'},
                    'question_id': {'type': 'string'},
                    'answer': {'type': 'string'}
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Respuesta guardada exitosamente'
        },
        403: {
            'description': 'Estudiante no registrado'
        }
    }
})
def submit_answer():
    """
    Endpoint para enviar respuestas de estudiantes
    ---
    tags:
      - answers
    """
    data = request.get_json()
    student_id = data.get('student_id')
    question_id = data.get('question_id')
    answer = data.get('answer')
    timestamp = time.time()
    
    if student_id not in students_db:
        students_db[student_id] = {}
    
    students_db[student_id][question_id] = {
        'answer': answer,
        'timestamp': timestamp,
        'graded': False,
        'score': 0
    }
    
    save_data(students_db, STUDENTS_FILE)
    return jsonify({'status': 'success', 'message': 'Respuesta guardada correctamente'})

@app.route('/grade/<student_id>', methods=['GET'])
def grade_student(student_id):
    if student_id not in students_db:
        return jsonify({'error': 'Estudiante no encontrado'}), 404
    
    student_answers = students_db[student_id]
    total_score = 0
    
    for question_type in questions_db:
        for question in questions_db[question_type]:
            q_id = question['id']
            if q_id in student_answers:
                if question['type'] == 'text':
                    answer = student_answers[q_id]['answer'].lower()
                    keywords_found = sum(1 for keyword in question['answer_key'] 
                                      if keyword.lower() in answer)
                    score = (keywords_found / len(question['answer_key'])) * question['points']
                    student_answers[q_id]['score'] = round(score, 2)
                    student_answers[q_id]['graded'] = True
                    total_score += score
    
    return jsonify({
        'student_id': student_id,
        'answers': student_answers,
        'total_score': round(total_score, 2)
    })

@app.route('/questions', methods=['GET'])
@swag_from({
    'responses': {
        200: {
            'description': 'Lista de preguntas disponibles',
            'schema': {
                'type': 'object',
                'properties': {
                    'theoretical': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {'type': 'string'},
                                'question': {'type': 'string'},
                                'points': {'type': 'integer'},
                                'type': {'type': 'string'},
                                'answer_key': {
                                    'type': 'array',
                                    'items': {'type': 'string'}
                                }
                            }
                        }
                    },
                    'problem_solving': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {'type': 'string'},
                                'question': {'type': 'string'},
                                'points': {'type': 'integer'},
                                'type': {'type': 'string'},
                                'answer_key': {
                                    'type': 'array',
                                    'items': {'type': 'string'}
                                }
                            }
                        }
                    },
                    'programming': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {'type': 'string'},
                                'question': {'type': 'string'},
                                'points': {'type': 'integer'},
                                'type': {'type': 'string'},
                                'test_cases': {
                                    'type': 'array',
                                    'items': {
                                        'type': 'object',
                                        'properties': {
                                            'setup': {'type': 'string'},
                                            'operations': {
                                                'type': 'array',
                                                'items': {'type': 'string'}
                                            },
                                            'expected': {'type': 'object'}
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
})
def get_questions():
    """
    Endpoint para obtener la lista de preguntas
    ---
    tags:
      - questions
    responses:
      200:
        description: Lista de preguntas disponibles
    """
    return jsonify(questions_db)

if __name__ == '__main__':
    app.run(debug=True)