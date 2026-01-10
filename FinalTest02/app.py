from flask import Flask, render_template, jsonify, request, redirect, url_for
import csv
import os

app = Flask(__name__)


# ESERCIZIO 1
# Funzione helper per leggere i dati dal file CSV e convertirli in una lista di dizionari
def get_all_events():
    events = []
    # Costruisce il percorso relativo alla cartella 'data'
    filepath = os.path.join('data', 'events.csv')
    
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            # DictReader usa la prima riga del CSV (header) come chiavi per i dizionari
            reader = csv.DictReader(file)
            for row in reader:
                events.append(row)

    except FileNotFoundError:
        # Se il file non esiste (es. primo avvio), restituisce una lista vuota
        return []
    
    return events


# ESERCIZIO #2
# Route principale: visualizzza la pagina HTML con la lista degli eventi
@app.route('/')
@app.route('/index')
def index():
    print("\n-----\nindex()...")
    print(f"Route [url, path]: \"{request.url}\",\"{request.path}\"")

    events = get_all_events()
    return render_template('index.html', events=events)


# ESERCIZIO #3
# Route dinamica: visualizza i dettagli di un singolo evento tramite il suo codice
@app.route('/event/<code>')
def event_detail(code):
    # Recupera l'eventuale messaggio di errore passato nella query string (es. ?alert=...)
    alert = request.args.get('alert')

    print("\n-----\nevent_detail(code)...")
    print(f"Route [url, path]: \"{request.url}\",\"{request.path}\"")
    print(f"Values received [code, alert]: \"{code}\",\"{alert}\"")

    events = get_all_events()
    
    # Trova l'evento con il codice specificato
    event = None
    for e in events:
        if e['code'] == code:
            event = e
            break
    
    return render_template('event_detail.html', event=event, alert=alert)


# ESERCIZIO #4
# Route per la gestione della prenotazione tramite form HTML
@app.route('/api/event/<code>', methods=['POST'])
def book_place(code):
    print("\n-----\nbook_place(code)...")
    print(f"Route [url, path]: \"{request.url}\",\"{request.path}\"")
    print(f"Values received [code]: \"{code}\"")
    
    if code:
        events = get_all_events()
        alert = None

        # Cerca l'evento e aggiorna il numero di posti
        for event in events:
            if code == event['code']:
                available_places = int(event['available_places'])

                # Verifica se ci sono ancora posti
                if available_places <= 0:
                    alert = "Non ci sono posti disponibili."
                    break

                # Decrementa e converte in stringa per la compatibilità con il file CSV
                event['available_places'] = str(available_places - 1)
        
        if not alert:
            # Aggiorna il file
            filepath = os.path.join('data', 'events.csv')
            with open(filepath, 'w', encoding='utf-8', newline='') as file:
                writer = csv.writer(file)

                writer.writerow(['code','name','sport','date','place','available_places'])      # Riscrive l'header

                # Riscrive tutte le righe aggiornate
                for event in events:
                    writer.writerow([
                        event['code'], event['name'], event['sport'],
                        event['date'], event['place'], event['available_places']
                        ])
                    
    # Dopo l'elaborazione del POST, reindirizza l'utente alla pagina dei dettagli
    return redirect(url_for('event_detail', code=code, alert=alert))


# ESERCIZIO #5
# API JSON: Restituisce la lista di tutti gli eventi (usata da React)
@app.route('/api/events')
def api_events():
    print("\n-----\napi_events()...")
    print(f"Route [url, path]: \"{request.url}\",\"{request.path}\"")

    events = get_all_events()
    return jsonify(events)


# ESERCIZIO #5
# API JSON per la prenotazione: viene chiamata da React tramite fetch()
@app.route('/api/book/<code>', methods=['POST'])
def api_book_place(code):
    print("\n-----\napi_book_place(code)...")
    print(f"Route [url, path]: \"{request.url}\",\"{request.path}\"")
    print(f"Values received [code]: \"{code}\"")

    events = get_all_events()
    event_found = None
    alert = None

    # Logica di aggiornamento (simile alla book_place ma per API, ovvero per risposte JSON)
    for event in events:
        if event['code'] == code:
            event_found = event
            available_places = int(event['available_places'])
            
            if available_places > 0:
                event['available_places'] = str(available_places - 1)
            else:
                alert = "Posti esauriti"

            break

    # Gestione errori in formato JSON per il frontend React
    if not event_found:
        return jsonify({
            "status": "error", 
            "message": "Evento non trovato"
        }), 404
    
    if alert:
        return jsonify({
            "status": "error", 
            "message": alert
        }), 400

    # Aggiorna il file CSV
    filepath = os.path.join('data', 'events.csv')
    with open(filepath, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        
        writer.writerow(['code','name','sport','date','place','available_places'])      # Riscrive l'header

        # Riscrive tutte le righe aggiornate
        for event in events:
            writer.writerow([
                event['code'], event['name'], event['sport'],
                event['date'], event['place'], event['available_places']
                ])

    # Ritorna successo in formato JSON (importante per React!)
    return jsonify({
        "status": "success", 
        "message": "Prenotazione completata", 
        "new_places": event_found['available_places']
    }), 200


# ESERCIZIO #6 e #7
# Route per la Single Page Application (SPA)
# <path:path> permette a Flask di ignorare i sottopercorsi (es. /react/event/E001),
# delegando la gestione della navigazione al React Router nel browser
@app.route('/react')
@app.route('/react/<path:path>')
def react_app(path=None):
    print("\n-----\nreact_app(code=None)...")
    print(f"Route [url, path]: \"{request.url}\",\"{request.path}\"")
    print(f"Values received [path]: \"{path}\"")

    # Restituisce sempre lo stesso template: il router di React deciderà cosa mostrare
    return render_template('index_react.html')


if __name__ == '__main__':
    # Avvia il server in modalità debug (si riavvia automaticamente alle modifiche)
    app.run(debug=True)
