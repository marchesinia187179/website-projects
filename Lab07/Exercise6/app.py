from flask import Flask, render_template, jsonify, request
import csv
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


def load_team_data():
    team_members = []
    csv_path = os.path.join(os.path.dirname(__file__), 'data/team.csv')

    try:
        with open(csv_path, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                team_members.append(row)
        return team_members
    
    except FileNotFoundError:
        print(f"Warning: {csv_path} not found")
        return []
    
    except Exception as e:
        print(f"Error loading team data: {e}")
        return []
    

@app.route('/team')
def team():
    team_members = load_team_data()
    return render_template('team.html', team_members=team_members)


def load_books_data():
    books = []
    csv_path = os.path.join(os.path.dirname(__file__), 'data/books.csv')

    try:
        with open(csv_path, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                books.append(row)
        return books
    
    except FileNotFoundError:
        print(f"Warning: {csv_path} not found")
        return []
    
    except Exception as e:
        print(f"Error loading books data: {e}")
        return []


# API GET
@app.route('/api/books', methods=['GET'])
def api_books():
    books = load_books_data()
    return jsonify(books)


# Add API to return a book by Title
@app.route('/title/books/<title>', methods=['GET'])
def api_book(title):
    books = load_books_data()
    for book in books:
        if book['Title'] == title:
            return jsonify(book)
    return jsonify({'error': 'Book not found'}), 404


# API POST
@app.route('/api/books', methods=['POST'])
def add_book_api():
    try:
        new_book = request.get_json()   # Get data from the request
        books = load_books_data()   # Load existing books

        # Validate incoming data
        if not all(key in new_book for key in ('Title', 'Author')):
            return jsonify({'error': 'Missing required fields'}), 400
        
        books.append(new_book)

        # Append to CSV file
        csv_path = os.path.join(os.path.dirname(__file__), 'data/books.csv')
        with open(csv_path, mode='a', encoding='utf-8', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=['Title', 'Author', 'Genre', 'Height', 'Publisher'])
            writer.writerow(new_book)   # Append new book

        return jsonify({'message': 'Book added successfully', 'book': new_book}), 201
    
    except Exception as e:
        return jsonify({'error', f'An error: {str(e)}'}), 500


@app.route('/books')
def books():
    books = load_books_data()
    return render_template('books.html', books=books)


if __name__ == '__main__':
    app.run(debug=True)