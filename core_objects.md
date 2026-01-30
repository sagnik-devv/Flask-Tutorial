1. REQUEST (Input) 
-------------------------------------------
WHAT IT IS: 
  The object that holds all data sent by the user (browser) to your server.

COMMON SYNTAX:
  value = request.form["name"]      # Get data from HTML form (POST)
  value = request.args.get("id")    # Get data from URL query string (GET)
  value = request.json              # Get JSON data (API calls)

WHEN TO USE:
  When you need to read what the user typed or clicked.

-------------------------------------------
2. RESPONSE (Output)
-------------------------------------------
WHAT IT IS:
  What your server sends back to the user's browser.

COMMON SYNTAX:
  return "<h1>Hello</h1>"           # Simple string/HTML response
  return render_template("idx.html")# Returning a full HTML file
  return Response(json_data)        # Custom response object (rarely needed for basic apps)

WHEN TO USE:
  At the end of every route function to show the user the result.

-------------------------------------------
3. REDIRECT (Navigation)
-------------------------------------------
WHAT IT IS:
  Forces the browser to load a different URL immediately.

COMMON SYNTAX:
  return redirect("/dashboard")
  return redirect(url_for("login")) # Best practice combined with url_for

WHEN TO USE:
  After a user submits a form (Post/Redirect/Get pattern) or logs in successfully.

-------------------------------------------
4. URL_FOR (Dynamic Links)
-------------------------------------------
WHAT IT IS:
  Generates the correct URL string based on the Python function name.

COMMON SYNTAX:
  link = url_for("home_page")       # Returns "/home" (if that's the route)
  link = url_for("profile", id=5)   # Returns "/profile/5"

WHEN TO USE:
  Anytime you need to link to another page. Never hardcode URLs (e.g., "/home") manually!

-------------------------------------------
5. SESSION (Memory)
-------------------------------------------
WHAT IT IS:
  A dictionary that saves data specific to a user across different page loads.

COMMON SYNTAX:
  app.secret_key = "xyz"            # Required setup
  session["user"] = "Sagnik"        # Save data
  current_user = session["user"]    # Read data
  session.pop("user", None)         # Delete data (Logout)

WHEN TO USE:
  To keep a user logged in or remember their shopping cart as they browse. 