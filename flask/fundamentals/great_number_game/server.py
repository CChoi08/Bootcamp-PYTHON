from flask import Flask, render_template, session, request, redirect
import random
app = Flask(__name__)
app.secret_key = 'pineapple chunks'

@app.route('/')
def guessHome():
    if 'randomNum' not in session:
        session['randomNum'] = random.randint(1,100)
        print(session['randomNum'])
    return render_template('index.html')

@app.route('/guess', methods = ['POST'])
def guess():
    session['guess'] = int(request.form['guess'])
    return redirect('/')

@app.route('/reset')
def playAgain():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug = True)