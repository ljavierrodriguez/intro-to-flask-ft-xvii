from flask import Flask, jsonify

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['ENV'] = 'development'

@app.route('/', methods=['GET']) # GET By Default
def main():
    return "Hola Mundo"

@app.route('/api/users', methods=['GET'])
def users():
    users = [{"id": 1, "name": "Luis"}]
    return jsonify(users), 204

if __name__ == '__main__':
    app.run()