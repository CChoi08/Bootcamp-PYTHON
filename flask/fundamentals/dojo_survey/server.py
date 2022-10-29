from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'pineapple chunks'


@app.route('/')
def survey():
    return render_template('index.html')

@app.route('/data', methods = ['POST'])
def userInput():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html')



if __name__ == '__main__':
    app.run(debug = True, port = 5001, host = 'localhost')