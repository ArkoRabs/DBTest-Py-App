from flask import Flask, render_template, request
import sqlite3
from datetime import datetime

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('club.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS members
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  fname TEXT NOT NULL,
                  lname TEXT NOT NULL,
                  email TEXT NOT NULL,
                  submitted_at TEXT NOT NULL)''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    fname = request.form['fname']
    lname = request.form['lname']
    email = request.form['email']
    submitted_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    conn = sqlite3.connect('club.db')
    c = conn.cursor()
    c.execute("INSERT INTO members (fname, lname, email, submitted_at) VALUES (?, ?, ?, ?)", (fname, lname, email, submitted_at))
    conn.commit()
    conn.close()
    return render_template('thank_you.html', fname=fname)

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)