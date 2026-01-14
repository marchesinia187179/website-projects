from flask import Flask, render_template, request, redirect, url_for, jsonify
import csv
import os
import ast

app = Flask(__name__)

# ESERCIZIO #1 - Funzioni per leggere i file CSV
def read_places():
    """Legge tutti i luoghi dal file places.csv"""
    places = []
    csv_path = os.path.join('data', 'places.csv')
    try:
        with open(csv_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['place_id'] = int(row['place_id'])
                row['price'] = float(row['price'])
                places.append(row)
    except FileNotFoundError:
        print(f"File {csv_path} non trovato")
    return places

def read_itineraries():
    """Legge tutti gli itinerari dal file itineraries.csv"""
    itineraries = []
    csv_path = os.path.join('data', 'itineraries.csv')
    try:
        with open(csv_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Converte place_list da stringa a lista
                row['itinerary_id'] = int(row['itinerary_id'])
                row['place_list'] = ast.literal_eval(row['place_list'])
                itineraries.append(row)
    except FileNotFoundError:
        print(f"File {csv_path} non trovato")

    return itineraries

def write_place_to_csv(place_data):
    """Scrive un nuovo luogo nel file places.csv"""
    csv_path = os.path.join('data', 'places.csv')
    file_exists = os.path.exists(csv_path)
    
    with open(csv_path, 'a', newline='', encoding='utf-8') as file:
        fieldnames = ['place_id', 'name', 'category', 'municipality', 'image_link', 'price']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        if not file_exists:
            writer.writeheader()
        
        writer.writerow(place_data)

def write_itinerary_to_csv(itinerary_data):
    """Scrive un nuovo itinerario nel file itineraries.csv"""
    csv_path = os.path.join('data', 'itineraries.csv')
    file_exists = os.path.exists(csv_path)
    
    with open(csv_path, 'a', newline='', encoding='utf-8') as file:
        fieldnames = ['itinerary_id', 'name', 'duration', 'place_list']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        if not file_exists:
            writer.writeheader()
        
        writer.writerow(itinerary_data)

def get_next_place_id():
    """Genera il prossimo place_id disponibile"""
    places = read_places()
    if not places:
        return 1
    
    max_id = 0
    for place in places:
        try:
            place_id = int(place['place_id'])
            if place_id > max_id:
                max_id = place_id
        except (ValueError, KeyError):
            continue
    
    return max_id + 1

def get_next_itinerary_id():
    """Genera il prossimo itinerary_id disponibile"""
    itineraries = read_itineraries()
    if not itineraries:
        return 1
    
    max_id = 0
    for itinerary in itineraries:
        try:
            itinerary_id = int(itinerary['itinerary_id'])
            if itinerary_id > max_id:
                max_id = itinerary_id
        except (ValueError, KeyError):
            continue
    
    return max_id + 1

def count_itineraries_for_place(place_id):
    """Conta quanti itinerari contengono un determinato luogo"""
    itineraries = read_itineraries()
    count = 0
    for itinerary in itineraries:
        if str(place_id) in itinerary.get('place_list', []):
            count += 1
    return count

# ESERCIZIO #2 - Route index modificata
@app.route('/')
@app.route('/index')
def index():
    places = read_places()
    return render_template('index.html', places=places)

# ESERCIZIO #3 - Pagina dedicata per ogni luogo
@app.route('/place/<int:place_id>')
def place_detail(place_id):
    places = read_places()
    place = None
    
    for p in places:
        if int(p['place_id']) == place_id:
            place = p
            break
    
    if place:
        # Conta gli itinerari che includono questo luogo
        itinerary_count = count_itineraries_for_place(place_id)
        place['itinerary_count'] = itinerary_count
    
    return render_template('place_detail.html', place=place)

# ESERCIZIO #4 - Form per aggiungere nuovo luogo
@app.route('/add_place')
def add_place_form():
    return render_template('add_place.html')

@app.route('/add_place', methods=['POST'])
def add_place():
    new_place_id = get_next_place_id()
    
    place_data = {
        'place_id': new_place_id,
        'name': request.form['name'],
        'category': request.form['category'],
        'municipality': request.form['municipality'],
        'image_link': request.form['image_link'],
        'price': request.form['price']
    }
    
    write_place_to_csv(place_data)
    return redirect(url_for('index'))

# ESERCIZIO #5 - API per itinerari
@app.route('/api/itineraries')
def api_itineraries():
    itineraries = read_itineraries()
    return jsonify(itineraries)

@app.route('/api/itinerary/<int:itinerary_id>/places')
def api_itinerary_places(itinerary_id):
    itineraries = read_itineraries()
    places = read_places()
    
    # Trova l'itinerario
    target_itinerary = None
    for itinerary in itineraries:
        if int(itinerary['itinerary_id']) == itinerary_id:
            target_itinerary = itinerary
            break
    
    if not target_itinerary:
        return jsonify({'error': 'Itinerary not found'}), 404
    
    # Trova i luoghi compresi nell'itinerario
    itinerary_places = []
    place_ids = target_itinerary.get('place_list', [])
    
    for place_id in place_ids:
        for place in places:
            if place['place_id'] == place_id:
                itinerary_places.append(place)
                break
    
    return jsonify(itinerary_places)

# ESERCIZIO #6 - Route per React SPA
@app.route('/react')
@app.route('/react/<path:path>')
def react_app(path=None):
    return render_template('index_react.html')

# ESERCIZIO #8 - API per aggiungere itinerario
@app.route('/api/places')
def api_places():
    places = read_places()
    return jsonify(places)

@app.route('/api/add_itinerary', methods=['POST'])
def api_add_itinerary():
    data = request.get_json()
    
    new_itinerary_id = get_next_itinerary_id()
    
    itinerary_data = {
        'itinerary_id': new_itinerary_id,
        'name': data['name'],
        'duration': data['duration'],
        'place_list': data['place_list']  # Mantieni come lista, sarà convertita in write_itinerary_to_csv
    }
    
    write_itinerary_to_csv(itinerary_data)
    return jsonify({'success': True, 'itinerary_id': new_itinerary_id})

if __name__ == '__main__':
    app.run(debug=True)