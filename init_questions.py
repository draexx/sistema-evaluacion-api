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

# Guardar las preguntas en un archivo JSON
with open('questions_data.json', 'w', encoding='utf-8') as f:
    json.dump(questions_db, f, indent=4, ensure_ascii=False)