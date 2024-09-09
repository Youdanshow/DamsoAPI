from flask import Flask, request, jsonify, redirect
from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from fastapi import Path, HTTPException

# mon api
app = Flask(__name__)

# modele
Base = declarative_base()
class Drink(Base):
    __tablename__ = 'drinks'

    drink_id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(String(50))

    def __repr__(self):
        return f'{self.name} - {self.description}'

# Configurer le moteur SQLAlchemy
db_uri = 'mysql+pymysql://root:Mazer0304_@localhost/flaskdb'
engine = create_engine(db_uri)

# Utiliser un scoped session
db_session = scoped_session(sessionmaker(bind=engine))

###############################################           début end point          #####################################################

########################## GET #############################
#end point root ma doc
@app.route("/docs")
def index():
    return redirect('http://localhost/api/docs/index.html')

#end point renvoie toute les boissons nom + description
@app.route("/drinks")
def get_drinks():
    drinks = db_session.execute(text('SELECT name, description FROM drinks'))

    output = []
    for drink in drinks:
        drink_data = {'name': drink.name, 'description': drink.description}
        output.append(drink_data)

    return {'drinks': output}

#end point renvoie la boisson à partir de l'id
@app.route("/drinks/<int:id>")
def get_drinks_by_id(id: int = Path(..., gt=-1)):
    drink = db_session.execute(text('SELECT * FROM drinks WHERE drink_id = :id'), {'id': id}).first()

    if drink:
        drink_data = {
            'name': drink.name,
            'description': drink.description
        }
        return jsonify(drink_data)
    else:
        return jsonify({'error': 'Drink not found'}), 404
    

########################## POST ############################
#end point ajoute une boisson à la base de données
@app.route('/add-drink', methods=['POST'])
def add_drink():
    data = request.get_json()
    
    if not data or 'drink_id' not in data or 'name' not in data or 'description' not in data:
        return jsonify({'error': 'Invalid input'}), 400
    
    id = data['drink_id']
    name = data['name']
    description = data['description']
    
    try:
        new_drink = Drink(drink_id=id, name=name, description=description)
        db_session.add(new_drink)
        db_session.commit()
        return jsonify({'message': 'Drink added successfully'}), 201
    except Exception as e:
        db_session.rollback()
        return jsonify({'error': str(e)}), 500
    

########################### DELETE #########################
#end point supprime une boisson de la base de données
@app.route('/del-drink/<int:id>', methods=['DELETE'])
def del_drink(id: int = Path(..., gt=-1)):
    try:
        # Exécuter une requête SQL pour récupérer la boisson par son ID
        deldrink = db_session.query(Drink).filter_by(drink_id=id).first()
            
        # Vérifier si la boisson existe
        if deldrink:
            db_session.delete(deldrink)
            db_session.commit()
            return jsonify({'message': 'Drink deleted successfully'}), 201
        else:
            return jsonify({'error drink not found': str(e)}), 500
    except Exception as e:
        db_session.rollback()
        return jsonify({'error': str(e)}), 500
    
###############################################           fin end point          #######################################################

# Fermeture de la session à la fin de la requête
@app.teardown_appcontext
def cleanup(resp_or_exc):
    db_session.remove()