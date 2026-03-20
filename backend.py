from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/rota-existente')
def rota_existente():
    return jsonify({'mensagem': 'Esta rota existe!'}), 200

if __name__ == '__main__':
    app.run(debug=True)
