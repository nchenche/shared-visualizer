from pathlib import Path
from flask import Flask, render_template
from flask_cors import CORS
from flask_socketio import SocketIO

from app.config import config_by_name, STATIC_PATH


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True, static_folder=STATIC_PATH)
    socketio = SocketIO(app)

    CORS(app)
    app.config.from_object(config_by_name[config_name])


    @app.route('/')
    def index():
        return render_template('index.html')

    @socketio.on('view_state')
    def handle_update_state(json):
        print('received update: ' + str(json))
        socketio.emit('view_state', json, include_self=False)    

    return app 