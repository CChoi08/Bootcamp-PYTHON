from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'dojo pineapple, keep it secret, keep it safe'

@app.route('/')
def counting():
    if "count" in session:
        session['count'] += 1
    else:
        session['count'] = 1
    return render_template('index.html', counter = session['count'])

@app.route('/add')
def addTwo():
    session['count'] += 1
    return redirect('/')

@app.route('/destroy')
def endSesh():
    session['count'] = 0
    return redirect('/')


if __name__ == '__main__':
    app.run(debug = True)