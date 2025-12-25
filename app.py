from flask import Flask

app= Flask(__name__) # __name__ is a special variable in Python that returns the name of the current module.

@app.route('/') # @app.route is a decorator that is used to bind a function to a URL.
def home(): # This is the function that will be called when the URL is accessed. 
    return 'Hello User this is my first flask app' # This is the response that will be sent back to the client. 
    

