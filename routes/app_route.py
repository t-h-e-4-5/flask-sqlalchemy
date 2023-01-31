from app import app
from flask import render_template

@app.route('/home')
def index():
    return render_template('data.html')

@app.route('/add')
def add():
    return render_template('form_add_user.html')
@app.route('/delete')
def delete():
    return render_template('delete.html')

@app.route('/by')
def get_id():
    #return render_template('find.html')
    return render_template('find_id.html')
@app.route('/user/up/')
def update_user():
    return render_template('update.html')
"""
@app.route('/')
def home():
    return render_template('pop.html')
"""