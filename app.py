from flask import Flask,render_template,url_for 

# 1. Initialize the Flask application
app = Flask(__name__)

# 2. Define a Route
# This function will be called when someone visits the root URL '/'
@app.route('/')
def home():
    return render_template("index.html")



# 3. Run the Application
if __name__ == '__main__':
    # debug=True allows the server to reload when you change code
    app.run(debug=True)
