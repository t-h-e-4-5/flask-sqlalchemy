from app import app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# Clé de hachage
app.config['SECRET_KEY'] = "bibi"
# app.config['MYSQL_DATABASE_USER']= "root"
# app.config['MYSQL_DATABASE_HOST']= "localhost"
# app.config['MYSQL_DATABASE_PASSWORD']= ""
# app.config['MYSQL_DATABASE_DB']= "db-sqlalchemy"
# Le lien de connextion a sqlalchemy
# %s pour passer les parametres
# username, password, host, nom de la base de donnée
# app.config['SQLALCHEMY_DATABASE_URI']= "mysql+pymysql://%s:%s@%s/%s"%('root','','localhost','3306','sqlalchemy-db')
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://theophile:123456789@localhost/sqlalchemy-db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# connexion  à la base de donnée
db = SQLAlchemy(app)

# db.init_app(app)
