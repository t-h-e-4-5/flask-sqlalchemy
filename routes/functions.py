from app import app
from config import db
from models import User
from flask import render_template, redirect, request, jsonify


@app.route('/user/add', methods=['POST'])
def add_user():
    try:
        # json = request.json
        data = request.form
        nom = data['nom']
        if nom and request.method == 'POST':
            user = User(nom=nom)
            db.session.add(user)
            db.session.commit()
            resultat = jsonify('Utilisateur ajouté ♠♦')
            return redirect('/home')
    except Exception as e:
        print(e)
        # resultat = {"code_status": 404, "message": 'Erreur frère'}
        return render_template('404.html')
    finally:
        db.session.rollback()
        db.session.close()


@app.route('/users', methods=['GET'])
def get_all():
    try:
        users = User.query.all()
        data = [{"id": user.id, "nom": user.nom} for user in users]
        # resultat = jsonify({"statut_code": 200,"users": data })
        resultat = jsonify(data)
        return resultat
    except Exception as e:
        print(e)
        # resultat = {"code_status": 404, "message": 'Erreur frère'}
        return render_template('404.html')
    finally:
        db.session.rollback()
        db.session.close()

"""
@app.route('/users/find/', methods=['POST'])
def get_user_by_id():
    try:
        data = request.form
        id = data['id']
        userID = User.query.filter_by(id=id).first()
        dat = {"id": userID.id, "nom": userID.nom}
        response = jsonify(dat)
        return response
    except Exception as e:
        print(e)
        return render_template('404.html')
    finally:
        db.session.rollback()
        db.session.close()
"""

@app.route('/users/delete/', methods=['POST'])
def delete_user():
    try:
        # json = request.json
        data = request.form
        id = data['id']
        # if id and request.method == 'DELETE':
        userID = User.query.filter_by(id=id).first()
        # user = User(id=id)
        db.session.delete(userID)
        db.session.commit()
        resultat = jsonify('Utilisateur supprimé ♠♦')
        return redirect('/home')
    except Exception as e:
        print(e)
        # resultat = {"code_status": 404, "message": 'Erreur frère'}
        return render_template('404.html')
    finally:
        db.session.rollback()
        db.session.close()


@app.route('/user/update/', methods=['POST', 'GET'])
def update():
    try:
        data = request.form
        id = data["id"]
        nom = data["nom"]
        user_id = User.query.filter_by(id=id).first()
        if id and nom and request.method == 'POST':
            user_id.nom = nom
            db.session.commit()
            return redirect('/home')
    except Exception as e:
        print(e)
        return render_template('404.html')
    finally:
        db.session.rollback()
        db.session.close()



@app.route('/users/find/<int:id>',methods = ['GET'])
def get_user_by_id(id):
    try:
        #data = request.form
        #id = data['id']
        userID = User.query.filter_by(id = id).first()
        dat = {"id" : userID.id, "nom": userID.nom} 
        response = jsonify(dat)        
        return response
    except Exception as e:
        print(e) 
        return render_template('404.html')
    finally:
        db.session.rollback()
        db.session.close()

""""
@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get(id)
    if not user:
        return render_template('404.html'), 404

    data = request.get_json()
    user.nom = data.get('nom')
    user.prenom = data.get('prenom')
    user.login = data.get('login')
    user.password = data.get('password')
    user.tel = data.get('tel')
    user.email = data.get('email')

    try:
        db.session.commit()
        response = jsonify({'status': 'Success', 'message': 'User updated successfully'})
        return response
    except Exception as e:
        db.session.rollback()
        response = jsonify({'status': 'Error', 'message': 'Error occured while updating user'})
        return response, 500


@app.route('/users/<int:id>',methods = ['GET','POST'])
def update_user(id):
    userID = User.query.filter_by(id = id).first()
    if request.method == 'GET':
        return render_template('update.html', user=userID)
    if request.method == 'POST':
        userID.nom = request.form['nom']
        db.session.commit()
        return redirect(url_for('get_all'))
"""
