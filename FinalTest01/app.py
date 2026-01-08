from flask import Flask, render_template, request, redirect, url_for, jsonify
import csv
import os

app = Flask(__name__)

# ESERCIZIO #1
# Funzione per leggere tutti i libri dal file library.csv
def get_all_books():
    """Legge e restituisce tutti i libri dal file library.csv"""
    books = []
    filepath = os.path.join('data', 'library.csv')
    
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                books.append(row)
    except FileNotFoundError:
        return []
    
    return books

# ESERCIZIO #1
# Funzione per leggere tutte le recensioni dal file reviews.csv
def get_all_reviews():
    """Legge e restituisce tutte le recensioni dal file reviews.csv"""
    reviews = []
    filepath = os.path.join('data', 'reviews.csv')
    
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                reviews.append(row)
    except FileNotFoundError:
        return []
    
    return reviews

# ESERCIZIO #2
# Route per visualizzare la lista dei libri
@app.route('/')
@app.route('/index')
def index():
    """Visualizza la pagina principale con la tabella dei libri"""
    books = get_all_books()
    return render_template('index.html', books=books)

# ESERCIZIO #3
# Route dinamica per visualizzare i dettagli di un libro
@app.route('/libro/<codice_libro>')
def book_detail(codice_libro):
    """Visualizza i dettagli di un libro specifico"""
    books = get_all_books()
    reviews = get_all_reviews()
    
    # Trova il libro con il codice specificato
    book = None
    for b in books:
        if b['code'] == codice_libro:
            book = b
            break
    
    # Filtra le recensioni per questo libro
    book_reviews = [r for r in reviews if r['book_code'] == codice_libro]
    
    return render_template('book_detail.html', book=book, reviews=book_reviews)

# ESERCIZIO #4
# Route per aggiungere una recensione
@app.route('/libro/<codice_libro>/add_review', methods=['POST'])
def add_review(codice_libro):
    """Aggiunge una nuova recensione al file reviews.csv"""
    username = request.form.get('username')
    text = request.form.get('text')
    
    if username and text:
        # Genera il codice della nuova recensione
        reviews = get_all_reviews()
        
        # Trova il numero più alto tra i codici esistenti
        max_num = 0
        for review in reviews:
            code = review['code']
            if code.startswith('R'):
                try:
                    num = int(code[1:])
                    if num > max_num:
                        max_num = num
                except ValueError:
                    pass
        
        # Genera il nuovo codice
        new_code = f"R{str(max_num + 1).zfill(3)}"
        
        # Aggiungi la recensione al file
        filepath = os.path.join('data', 'reviews.csv')
        with open(filepath, 'a', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([new_code, username, codice_libro, text])
    
    return redirect(url_for('book_detail', codice_libro=codice_libro))

# ESERCIZIO #5
# API per restituire tutti i libri in formato JSON
@app.route('/api/books')
def api_books():
    """API che restituisce tutti i libri in formato JSON"""
    books = get_all_books()
    return jsonify(books)

# ESERCIZIO #5
# API per restituire le recensioni di un libro specifico
@app.route('/api/reviews/<codice_libro>')
def api_reviews(codice_libro):
    """API che restituisce tutte le recensioni associate a un libro"""
    reviews = get_all_reviews()
    book_reviews = [r for r in reviews if r['book_code'] == codice_libro]
    return jsonify(book_reviews)

# ESERCIZIO #6 e #7
# Route per la SPA React
@app.route('/react')
@app.route('/react/')
@app.route('/react/book/<book_id>')
def react_app(book_id=None):
    """Renderizza l'applicazione React"""
    return render_template('index_react.html')

if __name__ == '__main__':
    app.run(debug=True)