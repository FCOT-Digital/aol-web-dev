from sqlite3 import connect
from flask import Flask, request, jsonify
import os

app = Flask(__name__)
script_dir = os.path.dirname(os.path.abspath(__file__))
database = os.path.join(script_dir, "db", "18_signup_my_database.db")

with connect(database) as connection:
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            email TEXT PRIMARY KEY,
            given_name TEXT NOT NULL
        )
    ''')

@app.route('/')
def home_page():
    return app.send_static_file('18_signup.html')

@app.route('/api/users', methods=['POST'])
def signup():
    data = request.get_json()
    given_name = data.get('given_name')
    email = data.get('email')

    if not given_name:
        return jsonify({'message': 'Missing name'}), 400
    if not email:
        return jsonify({'message': 'Missing email'}), 400

    with connect(database) as connection:
        cursor = connection.cursor()
        cursor.execute(
            'INSERT INTO users (email, given_name) VALUES (?, ?)',
            (email, given_name)
        )

    return jsonify({'message': 'Signed up successfully'}), 201

if __name__ == '__main__':
    app.run()
