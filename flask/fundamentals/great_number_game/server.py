from flask import Flask, render_template, session, request, redirect
import random
app = Flask(__name__)
app.secret_key = 'pineapple chunks'

@app.route('/')
def guessHome():
    for random_num in session:
        session['random_num'] = random.randint(1,100)
    return render_template('index.html', random_num = session['random_num'])

# @app.route('/wrong', method = ['POST'])
# def tooLow():
#     pass

# @app.route('/wrong', method = ['POST'])
# def tooHigh():
#     pass

if __name__ == '__main__':
    app.run(debug = True)