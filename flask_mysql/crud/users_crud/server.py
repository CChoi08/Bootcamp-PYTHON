from flask import Flask, render_template, request, redirect
from user_model import User

app = Flask(__name__)


@app.route('/')
def index():
    all_users = User.get_all()
    return render_template('/read.html', all_users = all_users)


@app.route('/users/new')
def new_user():
    return render_template('/create.html')


@app.route('/users/create', methods = ['POST'])
def create_user():
    user_id = User.create(request.form)
    return redirect('/')


@app.route('/users/<int:id>/show')
def show_user(id):
    one_user = User.get_one_user({'id':id})
    return render_template('user_show_one.html', one_user = one_user)


@app.route('/users/<int:id>/edit')
def edit_user(id):
    data = {
        'id' : id
    }
    this_user = User.get_one_user(data)
    return render_template('user_edit.html', this_user = this_user)


@app.route('/users/<int:id>/update', methods = ['POST'])
def update_user(id):
    data = {
        **request.form,
        'id' : id
    }
    User.update(data)
    return redirect('/')


@app.route('/users/<int:id>/delete')
def delete_user(id):
    data = {
        'id' : id
    }
    User.delete(data)
    # User.delete({'id':id}) can declare anonymously
    return redirect('/')



if __name__ == '__main__':
    app.run(debug = True)