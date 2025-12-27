from flask import Flask, request, redirect, url_for, Response, session

app = Flask(__name__)
app.secret_key = "super_secret_key"  # Required for session

@app.route('/', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        if username == "admin" and password == "admin":
            session["username"] = username
            return redirect(url_for('welcome'))
        else:
            return Response("Invalid credentials", status=401)
    
    # Return a simple login form for GET requests
    return '''
    <h1>Login</h1>
    <form method="post">
            <label>Username:</label> <input type="text" name="username"><br><br>
            <label>Password:</label> <input type="password" name="password"><br><br>
            <input type="submit" value="Login">
        </form>
    ''' 

@app.route('/welcome')
def welcome():
    if "username" in session:
        return f"Welcome {session['username']}!"
    else:
        return redirect(url_for('login')) 