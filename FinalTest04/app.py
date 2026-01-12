from flask import Flask, render_template, request, jsonify, redirect, url_for
import csv, os, inspect


app = Flask(__name__)


# ESERCIZIO #1
# Scrivere due funzioni che leggano e restituiscano 
# - tutti i video presenti nel file video.csv 
# - commenti presenti nel file comments.csv
def get_data(fileName):

    data = []
    filepath = os.path.join('data', fileName)

    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            data = list(csv.DictReader(file))

    except FileNotFoundError:
        print(f"Error: {fileName} not found")
        return []
    
    return data

def get_all_videos():
    return get_data('video.csv')

def get_all_comments():
    return get_data('comments.csv')

def get_video_comments(video_code):
    comments = get_all_comments()
    return [c for c in comments if c['video_code'] == video_code]


# ESERCIZIO #2
# Modificare la route /index per renderizzare un template index.html
@app.route('/')
@app.route('/index')
def index():
    videos = get_all_videos()
    comments = get_all_comments()

    # aggiunta del numero di commenti per video
    for video in videos:
        video['num_comments'] = len(get_video_comments(video['video_code']))

    return render_template('index.html', videos=videos)
    

# ESERCIZIO #3
# Pagina dedicata /video/<video_code> che mostri i dettagli del video corrispondente
@app.route('/video/<video_code>')
def video_detail(video_code):
    video = None
    comments = []

    for v in get_all_videos():
        if v['video_code'] == video_code:
            video = v
            break

    for c in get_all_comments():
        if c['video_code'] == video_code:
            comments.append(c['comment'])
    
    return render_template('video_detail.html', video=video, comments=comments)


# ESERCIZIO #4
# API Flask tramite il metodo POST per aggiungere un commento nuovo al video. 
# Aggiungere nel file comments.csv il nuovo commento associato al codice del video.
@app.route('/api/video/<video_code>', methods=['POST'])
def add_comment(video_code):
    new_comment = request.form.get('new_comment')
    filepath = os.path.join('data', 'comments.csv')

    try:
        with open(filepath, 'a', encoding='utf-8') as file:
            csv.writer(file).writerow([video_code, new_comment])

    except FileNotFoundError:
        print("Error: file not found")
        return []

    # Dopo l'elaborazione del POST, reindirizza l'utente alla pagina dei dettagli
    return redirect(url_for('video_detail', video_code=video_code))


# ESERCIZIO #6
# Creare due API:
# a. Una per restituire tutti i commenti in formato JSON.
# b. Una per restituire i commenti legati ad un solo video.
# Non è richiesto che ritorni anche la lista con le colonne del file, solo il dizionario contente i dati dei prodotti.

# API (a)
@app.route('/api/comments')
def api_comments():
    return jsonify(get_all_comments()[1:])

# API (b)
@app.route('/api/video_comments/<video_code>', methods=['POST'])
def api_video_comments(video_code):
    comments = get_all_comments()
    return jsonify(get_video_comments())


@app.route('/api/videos')
def api_videos():
    return jsonify(get_all_videos())


# ESERCIZIO #6
# Creare una route /react lato Flask per renderizzare il template index_react.html,
# dove costruire una Single Page Application (SPA) con React. 
# Tutte le route impostate con React devono seguire il prefisso /react
@app.route('/react')
@app.route('/react/<path:path>')
def react_app(video_code=None):
    return render_template('index_react.html')


# ESERCIZIO #8
# API Flask creata apposta per aggiungere un video nel file video.csv
@app.route('/api/video/add_video', methods=['POST'])
def add_video():
    data = request.get_json()
    
    if not data:
        return jsonify({'success': False, 'message': 'Dati mancanti'}), 400

    new_video_name = data.get('name')
    new_video_link = data.get('link')
    filepath = os.path.join('data', 'video.csv')

    new_video_code = len(get_all_videos()) + 1

    try:
        with open(filepath, 'a', encoding='utf-8') as file:
            csv.writer(file).writerow([new_video_code, new_video_name, new_video_link])

    except FileNotFoundError as e:
        print("Error: file not found")
        return jsonify({'success': False, 'message': str(e)}), 500
    
    return jsonify(get_all_videos())


if __name__ == '__main__':
    app.run(debug=True)
