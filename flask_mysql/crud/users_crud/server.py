from flask import Flask, render_template, request, redirect
from user import User

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



if __name__ == '__main__':
    app.run(debug = True)