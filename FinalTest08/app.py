from flask import Flask, render_template, request, redirect, url_for, jsonify
import csv
from datetime import datetime
import os

app = Flask(__name__)


# ESERCIZIO #1
# Scrivere due funzioni per leggere e restituire:
# (1) tutti i corsi presenti nel file courses.csv
# (2) tutte le prenotazioni presenti nel bookings.csv

# (1)
def get_courses():
    courses = []
    filepath = os.path.join('static/data', 'courses.csv')

    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            courses = list(csv.DictReader(file))
    except FileNotFoundError:
        print(f"Error: {filepath} not found")
        return []
    
    return courses

# (2)
def get_bookings():
    bookings = []
    filepath = os.path.join('static/data', 'bookings.csv')

    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            bookings = list(csv.DictReader(file))
    except FileNotFoundError:
        print(f"Error: {filepath} not found")
        return []
    
    return bookings


# ESERCIZIO #2
# Creare una route index per la visualizzazione di un template index.html
# una tabella contenente l’elenco dei corsi, se presenti. 
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', courses=get_courses())


# ESERCIZIO #3
# Reindirizzi alla seguente route dinamica: /course/<course_id>
@app.route('/course/<course_id>')
def course_detail(course_id):

    course = None
    for c in get_courses():
        if c['id'] == course_id:
            course = c
            break

    # aggiunta del numero di posti liberi
    nob = 0
    for booking in get_bookings():
        if booking['course_id'] == course_id:
            nob += 1
    
    course['total_free_places'] = int(course['total_places']) - nob
    
    return render_template('course_detail.html', course=course)


# ESERCIZIO #4
# L’id della prenotazione deve essere generato automaticamente.
# I dati della nuova prenotazione devono essere scritti nel file bookings.csv
@app.route('/api/book_course/<course_id>', methods=['POST'])
def book_course(course_id):
    nome = request.form.get('nome')
    cognome = request.form.get('cognome')

    booking_id = len(get_bookings()) + 1

    filepath = os.path.join('static/data', 'bookings.csv')

    try:
        with open(filepath, 'a', encoding='utf-8') as file:
            csv.writer(file).writerow([booking_id, course_id, nome, cognome])

    except FileNotFoundError:
        print("Error: file not found")
        return []

    # Dopo l'elaborazione del POST, reindirizza l'utente alla pagina dei dettagli
    return redirect(url_for('course_detail', course_id=course_id))


# ESERCIZIO #5
# Creare due API:
# (1) Una che restituisca tutti i corsi in formato JSON.
# (2) Una che restituisca tutte le prenotazioni associate a un corso specifico.

# (1)
@app.route('/api/courses')
def api_courses():
    return jsonify(get_courses()[1:])

# (2)
@app.route('/api/coursebookings/<course_id>')
def api_coursebookings(course_id):

    bookings = []
    for booking in get_bookings():
        if booking['course_id'] == course_id:
            bookings.append(booking)
    
    return jsonify(bookings)


# ESERCIZIO #7
# API POST per aggiungere un corso
# L’id del nuovo corso deve essere generato lato backend, i dati salvati nel file courses.csv
@app.route('/api/add_corse', methods=['POST'])
def add_question():
    data = request.get_json()
    
    if not data:
        return jsonify({'success': False, 'message': 'Dati mancanti'}), 400

    id = len(get_courses()) + 1
    name = data.get('name')
    instructor = data.get('instructor')
    hourstart = data.get('hourstart')
    hourend = data.get('hourend')
    places = data.get('places')

    days = []
    def add_day(d):
        if d != '':
            days.append(d)
    
    add_day(data.get('day1'))
    add_day(data.get('day2'))
    add_day(data.get('day3'))
    add_day(data.get('day4'))
    add_day(data.get('day5'))
    add_day(data.get('day6'))
    add_day(data.get('day7'))
    
    filepath = os.path.join('static/data', 'courses.csv')
    try:
        with open(filepath, 'a', encoding='utf-8') as file:
            csv.writer(file).writerow([
                id, name, instructor, days, f"{hourstart}-{hourend}", places])

    except FileNotFoundError as e:
        print("Error: file not found")
        return jsonify({'success': False, 'message': str(e)}), 500
    
    return jsonify(get_courses())


@app.route('/react')
def react_app(path=None):
    """
    Renderizza il template React SPA
    """
    return render_template('index_react.html')


if __name__ == '__main__':
    app.run(debug=True)
