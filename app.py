from flask import Flask, request, redirect, url_for, Response, session, render_template

# Initialize the Flask application
# 'app' is the instance of the Flask class that represents your web application.
# __name__ tells Flask where to look for resources like templates and static files.
app = Flask(__name__)

# Set a secret key for session management
# This is required to encrypt the session data stored in the browser's cookies.
# Without this, you cannot use 'session' to store user data (like login state).
app.secret_key = "super_secret_key"

# Define a route for valid users to see a welcome message
# @app.route connects a URL rule to a function.
@app.route('/hello')
def home():
    # This function runs when the user visits http://localhost:5000/hello
    return 'Hello User this is my first flask app'

# Define a generic 'About' page
@app.route('/about')
def about():
    return 'This is the about page'

# Define a generic 'Contact' page
@app.route('/contact')
def contact():
    return 'This is the contact page'

# Example of handling different HTTP methods (GET and POST)
@app.route("/submit", methods=["GET","POST"])
def submit():
    # Check if the browser sent a POST request (usually from a form submission)
    if request.method == "POST":
        return 'You send a POST request'
    else:
        # Default behavior for opening the page in a browser (GET request)
        return 'You send a GET request'

# The Main Login Route - This acts as the entry point (Root URL '/')
@app.route('/', methods=["GET", "POST"])
def login():
    # 1. Handle the Form Submission (POST)
    if request.method == "POST":
        # Retrieve data from the form inputs using their 'name' attributes
        username = request.form.get("username")
        password = request.form.get("password")
        
        # Simple hardcoded check for credentials
        if username == "admin" and password == "admin":
            # Store the username in the session (like a secure cookie)
            # This "logs them in" so we remember them on other pages.
            session["username"] = username
            
            # Redirect the user to the 'welcome' route
            # url_for('welcome') generates the URL for the function named 'welcome'
            return redirect(url_for('welcome'))
        else:
            # If login fails, return a 401 Unauthorized status
            return Response("Invalid credentials", status=401)
    
    # 2. Display the Login Form (GET)
    # This block runs when you first visit the page.
    return '''
    <h1>Login</h1>
    <!-- The form submits to the same URL ('/') using the POST method -->
    <form method="post">
            <label>Username:</label> <input type="text" name="username"><br><br>
            <label>Password:</label> <input type="password" name="password"><br><br>
            <input type="submit" value="Login">
        </form>
    ''' 

# Protected Welcome Page
# Protected Welcome Page
@app.route('/welcome')
def welcome():
    # Check if 'username' exists in the session (proving they logged in)
    if "username" in session:
        # Create a list of items to demonstrate loops in the template
        learning_list = ["Learn Flask", "Master Jinja2", "Build Cool Apps", "Explore SQLAlchemy"]
        
        # If logged in, greet them using their stored name AND render the template
        # We pass 'user' and 'items' as variables to the template
        return render_template('index.html', user=session['username'], items=learning_list)
    else:
        # If not logged in, kick them back to the login page
        return redirect(url_for('login')) 

# Main Execution Block
# This ensures the app only runs if this script is executed directly (not imported)
if __name__ == "__main__":
    # run(debug=True) starts the development server.
    # debug=True allows the server to auto-reload when you save code changes.
    app.run(debug=True)
