import os

from flask import Flask, render_template
from flask_migrate import Migrate
from Core.database import db
from Core.blueprints import users_bp

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///datab.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

migrate = Migrate(app, db)

app.register_blueprint(users_bp)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/users/<string:name>/homepage')
def homepage(name):
    return render_template('homepage.html', name=name)


if __name__ == '__main__':
    app.run(debug=True, port=81, host='0.0.0.0')
