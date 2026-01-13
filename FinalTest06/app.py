from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
import csv
import os
import random
from datetime import datetime

app = Flask(__name__)


# ESERCIZIO #1
# Scrivere due funzioni per leggere e restituire: 
# (1) Tutti i quiz presenti nel file quizzies.csv
# (2) Tutte le domande presenti nel file questions.csv

# (1)
def get_quizzies():
    quizzies = []
    filepath = os.path.join('data', 'quizzies.csv')

    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            quizzies = list(csv.DictReader(file))
    except FileNotFoundError:
        print(f"Error: {filepath} not found")
        return []
    
    return quizzies

# (2)
def get_questions():
    questions = []
    filepath = os.path.join('data', 'questions.csv')

    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            questions = list(csv.DictReader(file))
    except FileNotFoundError:
        print(f"Error: {filepath} not found")
        return []
    
    return questions


# ESERCIZIO #2
# Modificare la route /index per renderizzare un template index.html
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', quizzies=get_quizzies())


# ESERCIZIO #3
# L’applicazione dovrà selezionare automaticamente le domande tra quelle disponibili, 
# - senza ripetizioni
# - Inserire i dati del nuovo quiz nel file quizzies.csv
# 
# Nel caso il numero di domande inserito fosse più grande del numero di domande presenti, 
# - dovrà essere mandato un alert di errore.
@app.route('/api/add_quiz', methods=['POST'])
def add_quiz():
    quiz_name = request.form.get('quiz-name')
    question_count = int(request.form.get('question-count'))

    questions = get_questions()
    questions_selected = []

    quiz_code = f"QUIZ{len(get_quizzies()) + 1}"

    if question_count > len(questions):
        alert = f"Il numero di domande deve essere minore di {len(questions)}"
        return redirect(url_for('index', alert=alert))
    
    while len(questions_selected) < question_count:
        random_index = random.randrange(0, len(questions))
        random_question = questions[random_index]['question_code']

        if not questions_selected.__contains__(random_question):
            questions_selected.append(random_question)

    filepath = os.path.join('data', 'quizzies.csv')

    try:
        with open(filepath, 'a', encoding='utf-8') as file:
            csv.writer(file).writerow([quiz_code, quiz_name, questions_selected])

    except FileNotFoundError:
        print("Error: file not found")
        return []

    # Dopo l'elaborazione del POST, reindirizza l'utente alla pagina dei dettagli
    return redirect(url_for('index'))


# ESERCIZIO #4
# Reindirizzare l'utente a una pagina dedicata /quiz/<quiz_code> che mostri i dettagli del quiz. 
@app.route('/quiz/<quiz_code>')
def quiz_detail(quiz_code):

    quiz = None
    for q in get_quizzies():
        if q['quiz_code'] == quiz_code:
            quiz = q
            break

    questions = []
    for q in get_questions():
        if quiz['question_list'].__contains__(q['question_code']):
            questions.append(q)
    
    return render_template('quiz_detail.html', quiz=quiz, questions=questions)


# ESERCIZIO #6
# Creare due API: 
# (1) Una per restituire tutte le possibili domande in JSON. 
# (2) Una per restituire le domande legate a un quiz in JSON. 
# Non è richiesto che le API restituiscano anche le colonne del file, 
# ma solo un dizionario contenente i dati delle valutazioni.

# (1)
@app.route('/api/questions')
def api_questions():
    questions = get_questions()
    return jsonify(questions[1:])

# (2)
@app.route('/api/questions/<quiz_code>')
def api_questions_quiz(quiz_code):

    quiz = None
    for q in get_quizzies():
        if q['quiz_code'] == quiz_code:
            quiz = q
            break

    questions = []
    for q in get_questions():
        if quiz['question_list'].__contains__(q['question_code']):
            questions.append(q)

    return jsonify(questions)


# ESERCIZIO #6
# Creare una route /react lato Flask per renderizzare il template index_react.html
# Tutte le route impostate con React devono seguire il prefisso /react, 
# ad esempio /react/questions, /react/question/id, ecc
@app.route('/react')
@app.route('/react/<path:path>')
def react_app(path=None):
    return render_template('index_react.html')

# ESERCIZIO #8
# API POST per inserire una nuova domanda da React
@app.route('/api/add_question', methods=['POST'])
def add_question():
    data = request.get_json()
    
    if not data:
        return jsonify({'success': False, 'message': 'Dati mancanti'}), 400

    question_code = f"Q{len(get_questions()) + 1}"
    statement = data.get('enunciato')
    answer_1 = data.get('risposta1')
    answer_2 = data.get('risposta2')
    answer_3 = data.get('risposta3')
    answer_4 = data.get('risposta4')
    correct_answers = []

    def add_correct_answer(answer):
        if answer != '':
            correct_answers.append(int(answer))
    
    add_correct_answer(data.get('risposta1corretta'))
    add_correct_answer(data.get('risposta2corretta'))
    add_correct_answer(data.get('risposta3corretta'))
    add_correct_answer(data.get('risposta4corretta'))
    
    filepath = os.path.join('data', 'questions.csv')
    try:
        with open(filepath, 'a', encoding='utf-8') as file:
            csv.writer(file).writerow([
                question_code, statement, answer_1, answer_2, answer_3, answer_4, correct_answers])

    except FileNotFoundError as e:
        print("Error: file not found")
        return jsonify({'success': False, 'message': str(e)}), 500
    
    return jsonify(get_questions())


if __name__ == '__main__':
    app.run(debug=True)
