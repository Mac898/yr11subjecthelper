from flask_sqlalchemy import SQLAlchemy
# db variable initialization
db = SQLAlchemy()

def get_db():
    return db