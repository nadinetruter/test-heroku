from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_mail import Mail

from database.db import initialize_db
from flask_restful import Api
from resources.errors import errors


application = app = Flask(__name__)
app.config.from_pyfile('settings.py')
app.config["DEBUG"]= True
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USERNAME"] = "bytecare0@gmail.com"
app.config["MAIL_PASSWORD"] = "teambytecare0"
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSL"] = False
app.config["MAIL_DEFAULT_SENDER"]="bytecare0@gmail.com"

mail = Mail(app)
# imports requiring app and mail
from resources.routes import initialize_routes

api = Api(app)
api = Api(app, errors=errors)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)


app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb+srv://byteme:1234@cluster0.mlj40.mongodb.net/test?retryWrites=true&w=majority'
}

initialize_db(app)
initialize_routes(api)
