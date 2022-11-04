from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo_model import Dojo

@app.route('/')
def index():
    all_dojos = Dojo.get_all()
    return render_template('dashboard.html', all_dojos = all_dojos)


@app.route('/dojos/new')
def new_dojo():
    return render_template('/create_dojo.html')


@app.route('/dojos/create', methods = ['POST'])
def create_dojo():
    dojo_id = Dojo.create(request.form)
    return redirect('/')


@app.route('/dojos/<int:id>/show')
def show_dojo(id):
    one_dojo = Dojo.get_one_dojo({'id':id})
    return render_template('display_dojo.html', one_dojo = one_dojo)

