from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Configurer le moteur SQLAlchemy
db_uri = 'mysql+pymysql://root:Mazer0304_@localhost/flaskdb'
engine = create_engine(db_uri)

# Utiliser un scoped session
db_session = scoped_session(sessionmaker(bind=engine))

# Modèle
Base = declarative_base()
class Drink(Base):
    __tablename__ = 'drinks'

    drink_id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(String(50))

    def __repr__(self):
        return f'{self.name} - {self.description}'

# Sélectionner l'ID de la boisson à tester
id = 0

# Exécuter une requête SQL pour récupérer la boisson par son ID
drink = db_session.execute(text('SELECT * FROM drinks WHERE drink_id = :id'), {'id': id}).first()

# Vérifier si une boisson a été trouvée et afficher les résultats
if drink:
    drink_data = {
        'drink_id': drink.drink_id,
        'name': drink.name,
        'description': drink.description
    }
    print(drink_data)
else:
    print({'error': 'Drink not found'})

# Fermer la session
db_session.remove()
