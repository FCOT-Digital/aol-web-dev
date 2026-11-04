from flask import Flask

app = Flask(__name__)

@app.route('/')
def home_page():
    return app.send_static_file('16_index.html')

@app.route('/api/hello/<name>')
def hello_name(name):
    return f'Hello {name}, from Flask!'

if __name__ == '__main__':
    app.run()
