from flask import Flask, render_template, jsonify, request, redirect, url_for
import csv
import os

import inspect

app = Flask(__name__)


# ESERCIZIO #1
# Scrivere una funzione che legga e restituisca tutti i prodotti presenti nel file products.csv
def get_all_products():
    print(f"Debug: execution of {inspect.currentframe().f_code.co_name}")

    products = []
    filepath = os.path.join('data', 'products.csv')

    try:
        print(f"Debug: try to open {filepath}")
        with open(filepath, 'r', encoding='utf-8') as file:
            print("Ok: file open in read mode")

            # DictReader usa la prima riga del CSV (header) come chiavi per i dizionari
            reader = csv.DictReader(file)
            for row in reader:
                products.append(row)

    except FileNotFoundError:
        print("Error: file not found")
        return []
    
    print("Ok: data taken")
    return products


# Funzione aggiuntiva (non richiesta) che serve per aggiornare il file una volta modificato
def update_products(products):
    print(f"Debug: execution of {inspect.currentframe().f_code.co_name}")

    filepath = os.path.join('data', 'products.csv')

    print(f"Debug: try to open {filepath}")
    try:
        with open(filepath, 'w', encoding='utf-8', newline='') as file:
            print("Ok: file open in write mode")

            writer = csv.writer(file)

            # Riscrive l'header
            writer.writerow([
                'codice_prodotto','nome_prodotto','categoria',
                'prezzo','disponibilita','descrizione'])

            # Riscrive tutte le righe aggiornate
            for product in products:
                writer.writerow([
                    product['codice_prodotto'], product['nome_prodotto'], product['categoria'],
                    product['prezzo'], product['disponibilita'], product['descrizione']
                    ])
                
    except FileNotFoundError:
        print("Error: file not found")
        return []


# ESERCIZIO #2
# Modificare la route /index per renderizzare un template index.html
@app.route('/')
@app.route('/index')
def index():
    print(f"Debug: execution of {inspect.currentframe().f_code.co_name}")
    print(f"Route [url, path]: \"{request.url}\",\"{request.path}\"")

    products=get_all_products()
    return render_template('index.html', products=products)


# ESERCIZIO #3
# Reindirizzamento del utente a una pagina dedicata /product/<product_code> 
# che mostri i dettagli del prodotto corrispondente
@app.route('/product/<product_code>')
def product_detail(product_code):
    # Recupera l'eventuale messaggio di errore passato nella query string (es. ?alert=...)
    alert = request.args.get('alert')

    print(f"Debug: execution of {inspect.currentframe().f_code.co_name}")
    print(f"Route [url, path]: \"{request.url}\",\"{request.path}\"")
    print(f"Values received [product_code, alert]: \"{product_code}\",\"{alert}\"")
    
    # Trova il prodotto con il codice specificato
    product = None
    products = get_all_products()

    print("Debug: search product")
    for p in products:
        if p['codice_prodotto'] == product_code:
            print("Ok: product found")
            product = p
            break

    if not product:
        print("Error: product not found")
    
    return render_template('product_detail.html', product=product, alert=alert)


# ESERCIZIO #4
# API Flask /api/buy/<product_code> tramite il metodo POST. 
# Ridurre di uno la disponibilità del prodotto nel file products.csv.
# Gestire productuali errori, come la mancanza di disponibilità, 
# mostrando messaggi appropriati all’utente.
@app.route('/api/buy/<product_code>', methods=['POST'])
def buy_product(product_code):
    print(f"Debug: execution of {inspect.currentframe().f_code.co_name}")
    print(f"Route [url, path]: \"{request.url}\",\"{request.path}\"")
    print(f"Values received [product_code]: \"{product_code}\"")
    
    if product_code:
        products = get_all_products()
        alert = None

        # Cerca il prodotto e aggiorno la quantità
        print("Debug: searching product")
        for product in products:
            if product_code == product['codice_prodotto']:
                disponibilita = int(product['disponibilita'])

                # Verifica se è disponibile e se si aggiorna la quantità
                if disponibilita:
                    print("Ok: product available")
                    product['disponibilita'] = str(disponibilita - 1)
                else:
                    print("Error: product not available")
                    alert = "Prodotto non disponibile."               
        
        if not alert:
            update_products(products)
            
    # Dopo l'elaborazione del POST, reindirizza l'utente alla pagina dei dettagli
    return redirect(url_for('product_detail', product_code=product_code, alert=alert))


# ESERCIZIO #5
# Creare due API:
# a. Una per restituire tutti i prodotti in formato JSON.
# b. Una per restituire i dettagli di un singolo prodotto basandosi sul codice del prodotto.
# 
# ATTENZIONE (a): Non è richiesto che ritorni anche la lista con le colonne del file, 
# solo il dizionario contente i dati dei prodotti.

# API (a)
'''
@app.route('/api/products')
def api_products():
    print(f"Debug: execution of {inspect.currentframe().f_code.co_name}")
    print(f"Route [url, path]: \"{request.url}\",\"{request.path}\"")

    products = get_all_products()
    return jsonify(products)
'''

# Modifica dell'API (a) per gestire il filtro richiesto dall'ESERCIZIO #8
@app.route('/api/products')
def api_products():
    print(f"Debug: execution of {inspect.currentframe().f_code.co_name}")
    
    products = get_all_products()
    
    # 2. Legge il parametro 'name' dalla query string (es. /api/products?name=computer)
    query_name = request.args.get('name', '').lower()

    # 3. Se il campo contiene una stringa, filtra i prodotti (ESERCIZIO #8)
    if query_name:
        products = [
            p for p in products 
            if query_name in p.get('nome_prodotto', '').lower()
        ]
    
    # Se query_name è vuoto, restituisce automaticamente tutti i prodotti
    return jsonify(products)

# API (b)
@app.route('/api/book/<product_code>', methods=['POST'])
def api_book_place(product_code):
    print(f"Debug: execution of {inspect.currentframe().f_code.co_name}")
    print(f"Route [url, path]: \"{request.url}\",\"{request.path}\"")
    print(f"Values received [product_code]: \"{product_code}\"")

    products = get_all_products()
    product_found = None
    alert = None

    # Logica di aggiornamento (simile alla buy_product ma per API, ovvero per risposte JSON)
    for product in products:
        if product['codice_prodotto'] == product_code:
            product_found = product
            disponibilita = int(product['disponibilita'])
            
            if disponibilita > 0:
                product['disponibilita'] = str(disponibilita - 1)
            else:
                alert = "Esaurito"

            break

    # Gestione errori in formato JSON per il frontend React
    if not product_found:
        return jsonify({
            "status": "error", 
            "message": "Prodotto non trovato"
        }), 404
    
    if alert:
        return jsonify({
            "status": "error", 
            "message": alert
        }), 400

    # Aggiorna il file CSV
    update_products(products)

    # Ritorna successo in formato JSON (importante per React!)
    return jsonify({
        "status": "success", 
        "message": "Prodotto comprato", 
        "new_places": product_found['disponibilita']
    }), 200


# ESERCIZIO #6
# Creare una route /react lato Flask per renderizzare il template index_react.html, 
# dove costruire una Single Page Application (SPA) con React.
# Tutte le route impostate con React devono seguire il prefisso /react, ad esempio
# /react/product_detail, /react/buy, ecc.
@app.route('/react')
@app.route('/react/<path:path>')
def react_app(path=None):
    print(f"Debug: execution of {inspect.currentframe().f_code.co_name}")
    print(f"Route [url, path]: \"{request.url}\",\"{request.path}\"")
    print(f"Values received [path]: \"{path}\"")

    # Restituisce sempre lo stesso template: il router di React deciderà cosa mostrare
    return render_template('index_react.html')


if __name__ == '__main__':
    app.run(debug=True)
