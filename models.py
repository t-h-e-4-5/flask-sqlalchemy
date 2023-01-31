from config import db
# CLass User  ## Création de la table user avec les attributs
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True,  nullable=False)
    nom = db.Column(db.String(100),nullable=False)