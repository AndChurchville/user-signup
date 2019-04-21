from flask import Flask, render_template, request, redirect
import re

app = Flask(__name__)
app.config['DEBUG'] = True





@app.route("/signup")
def index():
    return render_template("base.html")

@app.route("/signup" , methods=['POST'])
def validate_signup():

    username = request.form['username']
    password = request.form['password']
    password2 = request.form['password2']
    email = request.form['email']

    username_error = ""
    password_error = ""
    password2_error = ""
    email_error = ""

    if not username:
        username_error = "Please enter a username"
    elif len(username) < 3 or len(username) > 20:
         username_error = "Not a valid username"
         username = ''
    else:
         hasSpace = True
         for char in username:
            if char.isspace():
                hasSpace = False
            if not hasSpace:
                username_error = "Username must not contain any spaces"
                username = ''
    
    if not password:
            password_error = "Please enter a password"
    elif len(password) < 3 or len(password) > 20:
            password_error = "Not a valid password"
    else: 
        hasSpace = True 
        for char in password:
            if char.isspace():
                 hasSpace = False
            if not hasSpace:
                password_error = "Password must not contain any spaces"
    
    if password != password2:
            password2_error = "Passwords must match"
    
    if not email:
        not email_error
    elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        email_error = "Not a valid email"
        email = ""
    else:
        if len(email) < 3 or len(email) > 20:
            email_error = "Not a valid email"

                
    
    if not username_error and not password_error and not password2_error and not email_error:
        return render_template('welcome.html', name=username)
    else:
        return render_template('base.html', username_error=username_error, password_error=password_error, password2_error=password2_error,
         email_error=email_error, username=username, email=email)   



    



app.run()