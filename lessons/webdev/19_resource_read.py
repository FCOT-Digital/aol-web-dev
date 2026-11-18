from sqlite3 import connect, Row
from flask import Flask, request, jsonify
import os

app = Flask(__name__)
script_dir = os.path.dirname(os.path.abspath(__file__))
database = os.path.join(script_dir, "db", "19_read.db")

with connect(database) as connection:
    cursor = connection.cursor()
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS users (
            email TEXT PRIMARY KEY,
            display_name TEXT NOT NULL,
            role TEXT NOT NULL
        )
        '''
    )
    cursor.execute(
        '''
        INSERT OR IGNORE INTO users
        (email, display_name, role)
        VALUES (?, ?, ?)
        ''',
        ('user@example.com', 'John Doe', 'SysAdmin')
    )

@app.route('/')
def home_page():
    return app.send_static_file('19_read.html')

@app.route('/api/users', methods=['GET'])
def list_users():
    with connect(database) as connection:
        connection.row_factory = Row
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM users')
        users = cursor.fetchall()
        return [dict(user) for user in users]

@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    display_name = data.get('display_name')
    email = data.get('email')

    if not display_name:
        return jsonify({'message': 'Missing name'}), 400
    if not email:
        return jsonify({'message': 'Missing email'}), 400

    with connect(database) as connection:
        cursor = connection.cursor()
        cursor.execute(
            'INSERT INTO users (email, display_name, role) VALUES (?, ?, ?)',
            (email, display_name, 'user')
        )

    return jsonify({'message': 'Signed up successfully'}), 201

if __name__ == '__main__':
    app.run()
