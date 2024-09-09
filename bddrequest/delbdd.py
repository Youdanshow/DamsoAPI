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

try:
    # Exécuter une requête SQL pour récupérer la boisson par son ID
    drink = db_session.query(Drink).filter_by(drink_id=id).first()
        
    # Vérifier si la boisson existe
    if drink:
        db_session.delete(drink)
        db_session.commit()
        print(f'Drink with id {id} deleted successfully')
    else:
        print(f'Error: Drink with id {id} not found')
except Exception as e:
    db_session.rollback()
    print(f'Error deleting drink: {e}')

# Fermer la session
db_session.remove()
