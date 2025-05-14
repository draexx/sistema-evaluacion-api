from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import time
import os

app = Flask(__name__)
CORS(app)  # Habilitar CORS para todas las rutas

# Lista de estudiantes registrados
registered_students = {
    "1": "SMITH JOHNSON MICHAEL JAMES",
    "2": "WILLIAMS BROWN EMMA SOPHIA",
    "3": "JONES GARCIA ALEXANDER DAVID",
    "4": "MILLER DAVIS OLIVIA GRACE",
    "5": "RODRIGUEZ MARTINEZ ETHAN LUCAS",
    "6": "HERNANDEZ LOPEZ ISABELLA AVA",
    "7": "GONZALEZ WILSON MASON NOAH",
    "8": "ANDERSON TAYLOR SOPHIA MIA",
    "9": "THOMAS MOORE WILLIAM JAMES",
    "10": "JACKSON WHITE EMILY GRACE",
    "11": "MARTIN HARRIS DANIEL JOSEPH",
    "12": "THOMPSON LEE VICTORIA ROSE",
    "13": "CLARK LEWIS CHRISTOPHER RYAN",
    "14": "ROBINSON WALKER ELIZABETH ANN",
    "15": "PEREZ HALL ANDREW THOMAS",
    "16": "YOUNG ALLEN MADISON CLAIRE",
    "17": "KING WRIGHT JOSHUA DAVID",
    "18": "SCOTT GREEN ASHLEY NICOLE",
    "19": "BAKER ADAMS JUSTIN TYLER",
    "20": "NELSON HILL RACHEL LAUREN",
}

# Base de datos en memoria para las respuestas de los estudiantes
students_db = {}

# Base de datos en memoria para las preguntas y respuestas correctas
questions_db = {
    "theoretical": [
        {
            "id": "1a",
            "question": "¿Qué es un TAD (Tipo Abstracto de Datos) y cuál es su importancia en la programación?",
            "points": 5,
            "type": "text",
            "answer_key": ["tipo abstracto", "datos", "encapsulamiento", "interfaz", "implementación"]
        },
        {
            "id": "1b",
            "question": "Diferencia entre estructuras de datos estáticas y dinámicas.",
            "points": 5,
            "type": "text",
            "answer_key": ["tamaño fijo", "tiempo de compilación", "tiempo de ejecución", "memoria dinámica"]
        },
        {
            "id": "1c",
            "question": "Principio LIFO (Last In, First Out) y mencione una aplicación práctica.",
            "points": 5,
            "type": "text",
            "answer_key": ["último en entrar", "primero en salir", "pila", "stack"]
        },
        {
            "id": "1d",
            "question": "Principio FIFO (First In, First Out) y mencione una aplicación práctica.",
            "points": 5,
            "type": "text",
            "answer_key": ["primero en entrar", "primero en salir", "cola", "queue"]
        },
        {
            "id": "2a",
            "question": "Explique la diferencia entre una pila implementada con arreglos y una pila implementada con nodos enlazados. Mencione ventajas y desventajas de cada implementación.",
            "points": 5,
            "type": "text",
            "answer_key": ["arreglo", "fijo", "nodo", "enlace", "dinámico", "memoria", "puntero"]
        },
        {
            "id": "2b",
            "question": "¿Qué es una cola circular y qué problema resuelve respecto a una cola implementada con un arreglo simple?",
            "points": 5,
            "type": "text",
            "answer_key": ["circular", "reutilizar", "espacio", "índice", "módulo", "frente", "final"]
        },
        {
            "id": "2c",
            "question": "Explique el concepto de desbordamiento (overflow) y subdesbordamiento (underflow) en las estructuras de datos y cómo manejarlos.",
            "points": 5,
            "type": "text",
            "answer_key": ["overflow", "llena", "underflow", "vacía", "excepción", "control"]
        },
        {
            "id": "2d",
            "question": "¿Cuál es la importancia de la modularidad al implementar estructuras de datos como pilas y colas?",
            "points": 5,
            "type": "text",
            "answer_key": ["reutilización", "mantenimiento", "encapsulamiento", "abstracción", "interfaz"]
        }
    ],
    "problem_solving": [
        {
            "id": "3",
            "question": "Dada la siguiente secuencia de operaciones sobre una pila inicialmente vacía, indique el contenido final de la pila (si hay alguno) y dibuje el estado de la pila después de cada operación: push(10), push(20), pop(), push(30), push(40), pop(), push(50), pop()",
            "points": 15,
            "type": "text",
            "answer_key": ["10, 30", "[10, 30]"]
        },
        {
            "id": "4a",
            "question": "Trace la ejecución de las siguientes operaciones sobre una cola circular implementada con un arreglo de tamaño 5, inicialmente vacía. Indique en cada paso los valores de frente y final, así como el contenido del arreglo: encolar(10), encolar(20), desencolar(), encolar(30), encolar(40), desencolar(), encolar(50), encolar(60), desencolar(), encolar(70)",
            "points": 10,
            "type": "text",
            "answer_key": ["frente = 3", "final = 2", "40, 50, 60, 70"]
        },
        {
            "id": "4b",
            "question": "¿Qué sucedería si intentamos encolar un elemento más? Explique la situación de desbordamiento en una cola circular e indique cómo podría resolverse.",
            "points": 10,
            "type": "text",
            "answer_key": ["desbordamiento", "overflow", "llena", "redimensionar", "dinámico"]
        }
    ],
    "programming": [
        {
            "id": "5",
            "question": "Implemente una cola de doble extremo (deque) en Python usando una clase con los métodos: inicializar(), esta_vacia(), insertar_frente(elemento), insertar_final(elemento), eliminar_frente(), eliminar_final(), tamano()",
            "points": 25,
            "type": "code",
            "test_cases": [
                {
                    "setup": "deque = DequeDobleExtremo()",
                    "operations": [
                        "deque.insertar_frente(10)",
                        "deque.insertar_final(20)",
                        "result1 = deque.eliminar_frente()",
                        "result2 = deque.eliminar_final()"
                    ],
                    "expected": {"result1": 10, "result2": 20}
                },
                {
                    "setup": "deque = DequeDobleExtremo()",
                    "operations": [
                        "deque.insertar_final(30)",
                        "deque.insertar_final(40)",
                        "deque.insertar_frente(20)",
                        "deque.insertar_frente(10)",
                        "size = deque.tamano()",
                        "result1 = deque.eliminar_frente()",
                        "result2 = deque.eliminar_final()",
                        "size_after = deque.tamano()"
                    ],
                    "expected": {"size": 4, "result1": 10, "result2": 40, "size_after": 2}
                }
            ]
        }
    ]
}

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(registered_students)

# Rutas de archivos JSON
STUDENTS_FILE = 'students_data.json'
QUESTIONS_FILE = 'questions_data.json'

def load_data():
    # Cargar datos de estudiantes
    if os.path.exists(STUDENTS_FILE):
        with open(STUDENTS_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_data(data):
    # Guardar datos de estudiantes
    with open(STUDENTS_FILE, 'w') as f:
        json.dump(data, f, indent=4)

# Cargar datos al inicio
students_db = load_data()

@app.route('/submit', methods=['POST'])
def submit_answer():
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
    
    # Guardar los datos en el archivo JSON
    save_data(students_db)
    
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
                    # Calificar preguntas teóricas basadas en palabras clave
                    answer = student_answers[q_id]['answer'].lower()
                    keywords_found = sum(1 for keyword in question['answer_key'] 
                                      if keyword.lower() in answer)
                    score = (keywords_found / len(question['answer_key'])) * question['points']
                    student_answers[q_id]['score'] = round(score, 2)
                    student_answers[q_id]['graded'] = True
                    total_score += score
                elif question['type'] == 'code':
                    # Para preguntas de programación, ejecutar casos de prueba
                    # Aquí deberías implementar la lógica de evaluación de código
                    pass
    
    return jsonify({
        'student_id': student_id,
        'answers': student_answers,
        'total_score': round(total_score, 2)
    })

@app.route('/questions', methods=['GET'])
def get_questions():
    return jsonify(questions_db)

if __name__ == '__main__':
    app.run(debug=True)