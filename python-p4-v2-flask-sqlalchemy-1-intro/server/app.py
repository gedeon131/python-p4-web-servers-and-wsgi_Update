from flask import Flask
from flask_migrate import Migrate

from models import db

# create a Flask application instance
app = Flask(__name__)

# configure the database connection to the local file app.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

# configure flag to disable modification tracking and use less memory
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# create a Migrate object to manage schema modifications
migrate = Migrate(app, db)

# initialize the Flask application to use the database
db.init_app(app)

# ----------------------------------------
# ✅ Route par défaut
@app.route('/')
def index():
    return '<h1>Bienvenue sur Flask + SQLAlchemy!</h1>'

# ✅ Facultatif : Exécute le serveur avec `python app.py`
if __name__ == '__main__':
    app.run(port=5555, debug=True)



if __name__ == '__main__':
    app.run(port=5555, debug=True)
from flask import jsonify
from models import Pet  # Assure-toi que Pet est bien importé

@app.route('/pets', methods=['GET'])
def get_pets():
    pets = Pet.query.all()
    pets_list = [
        {"id": pet.id, "name": pet.name, "species": pet.species}
        for pet in pets
    ]
    return jsonify(pets_list), 200
