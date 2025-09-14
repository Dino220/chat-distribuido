import os
from flask import Flask, render_template, request
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")  # muy importante para conectar con AwardSpace

@app.route('/')
def index():
    return "Servidor SocketIO activo en Render 🚀"

@socketio.on('message')
def handle_message(data):
    print(f"[RECV] {data}")
    send({'msg': data['msg'], 'user': data['user']}, broadcast=True)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    socketio.run(app, host="0.0.0.0", port=port)
