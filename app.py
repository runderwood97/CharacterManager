import eventlet

eventlet.monkey_patch()

from flask_socketio import SocketIO
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_login import LoginManager, login_required, login_user, current_user

app = Flask(__name__)
app.config['DEBUG'] = True
app.config["LOGIN_DISABLED"] = False
app.config["SECRET_KEY"] = "herbalism"

socketio = SocketIO()

#socketio.init_app(app, async_mode='eventlet', cors_allowed_origins = ["https://streamapp.ejwatercoop.com", "https://stream.ejwatercoop.com"], async_handlers = True)
socketio.init_app(app, async_mode='eventlet', logger = True, engineio_logger = True, async_handlers = True)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "validate_user"