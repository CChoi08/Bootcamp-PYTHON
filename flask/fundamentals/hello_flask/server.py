from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

# import statements, maybe some other routes
    
@app.route('/dojo')
def dojo():
  return "Dojo!"

@app.route('/say/<name>') # for a route '/Hi/____' anything after '/hello/' gets passed as a variable 'name'
def say(name):
    print(name)
    return "Hi, " + name + "!"

@app.route('/users/<x>/<saying>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def show_user_profile(x, saying):
    print(int(x))
    print(saying)
    return x * saying


# app.run(debug=True) should be the very last statement! 

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

