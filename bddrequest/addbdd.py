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

id=3
name = "dog"
description = "dog drink"

# Ajouter une nouvelle boisson
try:
    new_drink = Drink(drink_id=id, name=name, description=description)
    db_session.add(new_drink)
    db_session.commit()
    print(f'Drink {name} added successfully')
except Exception as e:
    db_session.rollback()
    print(f'Error adding drink: {e}')

# Fermer la session
db_session.remove()
