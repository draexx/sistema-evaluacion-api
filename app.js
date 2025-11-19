class ExamApp {
    constructor() {
        this.questions = {};
        this.studentAnswers = {};
        this.students = {};
        this.init();
    }

    async init() {
        await Promise.all([
            this.loadQuestions(),
            this.loadStudents()
        ]);
        this.setupEventListeners();
        this.renderQuestions();
    }

    async loadStudents() {
        try {
            const response = await fetch('http://127.0.0.1:5000/students');
            this.students = await response.json();
            this.populateStudentSelect();
        } catch (error) {
            console.error('Error al cargar la lista de estudiantes:', error);
        }
    }

    populateStudentSelect() {
        const select = document.getElementById('studentId');
        select.innerHTML = '<option value="">Seleccione un estudiante</option>';
        for (const [id, name] of Object.entries(this.students)) {
            const option = document.createElement('option');
            option.value = id;
            option.textContent = name;
            select.appendChild(option);
        }
    }

    async loadQuestions() {
        try {
            const response = await fetch('http://127.0.0.1:5000/questions');
            this.questions = await response.json();
        } catch (error) {
            console.error('Error al cargar las preguntas:', error);
        }
    }

    setupEventListeners() {
        document.getElementById('submitBtn').addEventListener('click', () => this.submitAnswers());
        document.getElementById('gradeBtn').addEventListener('click', () => this.getGrade());
    }

    renderQuestions() {
        const container = document.getElementById('questionsContainer');
        container.innerHTML = '';

        // Renderizar preguntas teóricas
        this.renderQuestionSection('theoretical', 'Preguntas Teóricas');
        
        // Renderizar problemas
        this.renderQuestionSection('problem_solving', 'Resolución de Problemas');
        
        // Renderizar programación
        this.renderQuestionSection('programming', 'Programación');
    }

    renderQuestionSection(section, title) {
        const container = document.getElementById('questionsContainer');
        const questions = this.questions[section];

        const sectionDiv = document.createElement('div');
        sectionDiv.className = 'section';
        sectionDiv.innerHTML = `<h2>${title}</h2>`;

        questions.forEach(question => {
            const questionCard = document.createElement('div');
            questionCard.className = 'question-card';
            questionCard.innerHTML = `
                <div class="question-text">${question.question}</div>
                <div class="points">Puntos: ${question.points}</div>
                <textarea 
                    id="answer-${question.id}" 
                    placeholder="Escribe tu respuesta aquí..."
                ></textarea>
            `;
            sectionDiv.appendChild(questionCard);
        });

        container.appendChild(sectionDiv);
    }

    async submitAnswers() {
        const studentId = document.getElementById('studentId').value;
        if (!studentId) {
            alert('Por favor, seleccione un estudiante');
            return;
        }

        const answers = this.collectAnswers();
        
        try {
            // Deshabilitar el formulario antes de enviar
            this.disableForm();

            for (const questionId in answers) {
                await fetch('http://127.0.0.1:5000/submit', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        student_id: studentId,
                        question_id: questionId,
                        answer: answers[questionId]
                    })
                });
            }

            alert('Respuestas enviadas correctamente');
            
            // Mantener el formulario deshabilitado
            document.getElementById('submitBtn').style.display = 'none';
            document.getElementById('gradeBtn').style.display = 'block';
            
        } catch (error) {
            console.error('Error al enviar respuestas:', error);
            // En caso de error, volver a habilitar el formulario
            this.enableForm();
            alert('Error al enviar las respuestas. Por favor, intente nuevamente.');
        }
    }

    disableForm() {
        // Deshabilitar el selector de estudiantes
        document.getElementById('studentId').disabled = true;
        
        // Deshabilitar todas las áreas de texto
        const textareas = document.querySelectorAll('textarea');
        textareas.forEach(textarea => {
            textarea.disabled = true;
        });
        
        // Deshabilitar el botón de enviar
        document.getElementById('submitBtn').disabled = true;
    }

    enableForm() {
        // Habilitar el selector de estudiantes
        document.getElementById('studentId').disabled = false;
        
        // Habilitar todas las áreas de texto
        const textareas = document.querySelectorAll('textarea');
        textareas.forEach(textarea => {
            textarea.disabled = false;
        });
        
        // Habilitar el botón de enviar
        document.getElementById('submitBtn').disabled = false;
    }

    collectAnswers() {
        const answers = {};
        const textareas = document.querySelectorAll('textarea');
        textareas.forEach(textarea => {
            const questionId = textarea.id.replace('answer-', '');
            answers[questionId] = textarea.value;
        });
        return answers;
    }

    async getGrade() {
        const studentId = document.getElementById('studentId').value;
        if (!studentId) {
            alert('Por favor, ingresa tu ID de estudiante');
            return;
        }

        try {
            const response = await fetch(`http://127.0.0.1:5000/grade/${studentId}`);
            const grade = await response.json();
            this.displayGrade(grade);
        } catch (error) {
            console.error('Error al obtener la calificación:', error);
        }
    }

    displayGrade(grade) {
        const gradeContainer = document.getElementById('gradeContainer');
        const gradeDetails = document.getElementById('gradeDetails');

        let html = `
            <h3>Calificación Total: ${grade.total_score}</h3>
            <table class="grade-table">
                <thead>
                    <tr>
                        <th>Pregunta</th>
                        <th>Tu Respuesta</th>
                        <th>Puntuación</th>
                    </tr>
                </thead>
                <tbody>
        `;

        for (const questionId in grade.answers) {
            const answer = grade.answers[questionId];
            const question = this.findQuestionById(questionId);
            html += `
                <tr>
                    <td>${question.question}</td>
                    <td>${answer.answer}</td>
                    <td>${answer.score} / ${question.points}</td>
                </tr>
            `;
        }

        html += '</tbody></table>';
        gradeDetails.innerHTML = html;
        gradeContainer.style.display = 'block';
    }

    findQuestionById(id) {
        for (const section in this.questions) {
            const question = this.questions[section].find(q => q.id === id);
            if (question) {
                return question;
            }
        }
        return null;
    }
}

// Inicializar la aplicación
document.addEventListener('DOMContentLoaded', () => {
    new ExamApp();
});