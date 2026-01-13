import csv, os
from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)


# ESERCIZIO #1
# Scrivere due funzioni per leggere e restituire: 
# - Tutti i videogiochi presenti nel file videogames.csv
# - Tutte le valutazioni presenti nel file ratings.csv
def get_videogames():

    videogames = []
    filepath = os.path.join('data', 'videogames.csv')

    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            videogames = list(csv.DictReader(file))

    except FileNotFoundError:
        print(f"Error: {filepath} not found")
        return []
    
    return videogames

def get_ratings():

    ratings = []
    filepath = os.path.join('data', 'ratings.csv')

    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            ratings = list(csv.DictReader(file))

    except FileNotFoundError:
        print(f"Error: {filepath} not found")
        return []
    
    return ratings


# ESERCIZIO #2
# Modificare la route /index per renderizzare un template index.html
# Calcolare la media delle valutazioni associate a ogni singolo videogioco.
# Nel caso in cui il videogioco non abbia valutazioni, visualizzare il messaggio “nessuna valutazione disponibile”.
@app.route('/')
@app.route('/index')
def index():
    videogames = get_videogames()
    ratings = get_ratings()

    # calcolo della media delle valutazioni
    for videogame in videogames:
        sum_ratings = 0
        count_ratings = 0

        for rating in ratings:
            if rating['videgame_code'] == videogame['code']:
                sum_ratings += float(rating['rating'])
                count_ratings += 1

        # aggiunta della media delle valutazioni
        if count_ratings:
            videogame['avarage_rating'] = f"{sum_ratings / count_ratings:.2f}"
        else:
            videogame['avarage_rating'] = "nessuna valutazione disponibile"

    return render_template('index.html', videogames=videogames)


# ESERCIZIO #3
# Quando un utente clicca su un videogioco, 
# reindirizzarlo a una pagina dedicata /videogame/<game_code> che 
# mostri i dettagli del videogioco corrispondente, formattati in modo chiaro e leggibile. 
@app.route('/videogame/<game_code>')
def videogame_detail(game_code):
    videogame = None
    ratings = []

    for v in get_videogames():
        if v['code'] == game_code:
            videogame = v
            break

    for r in get_ratings():
        if r['videgame_code'] == game_code:
            ratings.append(r)
    
    return render_template('videogame_detail.html', videogame=videogame, ratings=ratings)


# ESERCIZIO #4
# API Flask tramite il metodo POST per aggiungere una nuova valutazione al videogioco. 
# Il nuovo dato deve essere aggiunto al file ratings.csv, associato al codice del videogioco. 
@app.route('/api/videogame/<game_code>', methods=['POST'])
def add_rating(game_code):
    username = request.form.get('username')
    rating = request.form.get('valutazione')

    filepath = os.path.join('data', 'ratings.csv')

    try:
        with open(filepath, 'a', encoding='utf-8') as file:
            csv.writer(file).writerow([username, game_code, rating])

    except FileNotFoundError:
        print("Error: file not found")
        return []

    # Dopo l'elaborazione del POST, reindirizza l'utente alla pagina dei dettagli
    return redirect(url_for('videogame_detail', game_code=game_code))


# ESERCIZIO #5
# Creare due API: 
# (1) Una per restituire tutte le valutazioni in formato JSON. 
# (2) Una per restituire le valutazioni legate a un solo videogioco. 
# Non è richiesto che le API restituiscano anche le colonne del file, 
# ma solo un dizionario contenente i dati delle valutazioni.

# (1)
@app.route('/api/ratings')
def api_ratings():
    ratings = get_ratings()
    return jsonify(ratings[1:])

# (2)
@app.route('/api/ratings/<game_code>')
def api_ratings_videogame(game_code):
    ratings = get_ratings()
    videogame_ratings = [r for r in ratings if r['videgame_code'] == game_code]
    return jsonify(videogame_ratings)


# ESERCIZIO #6
# Creare una route /react lato Flask per renderizzare il template index_react.html, 
# dove costruire una Single Page Application (SPA) con React. 
# Tutte le route impostate con React devono seguire il prefisso /react
@app.route('/react')
@app.route('/react/<path:path>')
def react_app(path=None):
    return render_template('index_react.html')


# ESERCIZIO #7
# API per restituire tutti i videogames in formato JSON
@app.route('/api/videogames')
def api_videogames():
    return jsonify(get_videogames())


# ESERCIZIO #8
# Il codice deve essere generato automaticamente lato backend all'interno di un'API 
# Flask creata appositamente per aggiungere il videogioco nel file videogames.csv
@app.route('/api/video/add_videogame', methods=['POST'])
def add_videogame():
    data = request.get_json()
    
    if not data:
        return jsonify({'success': False, 'message': 'Dati mancanti'}), 400

    new_videogame_name = data.get('name')
    new_videogame_company = data.get('company')
    filepath = os.path.join('data', 'videogames.csv')

    new_videogame_code = len(get_videogames()) + 1

    try:
        with open(filepath, 'a', encoding='utf-8') as file:
            csv.writer(file).writerow([new_videogame_code, new_videogame_name, new_videogame_company])

    except FileNotFoundError as e:
        print("Error: file not found")
        return jsonify({'success': False, 'message': str(e)}), 500
    
    return jsonify(get_videogames())


if __name__ == '__main__':
    app.run(debug=True)
