from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def checkerboard():
    return render_template('index.html')

@app.route('/<int:times>')
def yaxis(times):
    return render_template('index.html', times = times)

if __name__=="__main__": 
    app.run(debug=True)