from flask import Flask, render_template
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


@app.route('/team')
def team():
    team_members = [
        {
            'name': 'Doggo',
            'position': 'Founder and CEO',
            'email': 'doggo@company.com',
            'image': 'doggo.jpg'
        },
        {
            'name': 'Bunny',
            'position': 'COO',
            'email': 'bunny@company.com',
            'image': 'bunny.jpg'
        },
        {
            'name': 'Gattech',
            'position': 'Lead Engineer',
            'email': 'gattech@company.com',
            'image': 'gattech.jpeg'
        }
    ]
    return render_template('team.html', team_members=team_members)


if __name__ == '__main__':
    app.run(debug=True)