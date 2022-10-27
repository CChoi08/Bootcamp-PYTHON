from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello'

@app.route('/play')
def play():
    return render_template('index.html')

@app.route('/play/<int:times>')
def print_blocks(times):
    return render_template('index.html', times = times)

@app.route('/play/<int:times>/<color>')
def print_color_blocks(times, color = 'red'):
    return render_template('index.html', times = times, color = color)

if __name__ == '__main__':
    app.run(debug = True, port='5001')