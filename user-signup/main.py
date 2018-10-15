from flask import Flask, request, redirect, render_template, url_for
import cgi
import re


app = Flask(__name__)
app.config['DEBUG'] = True

page_header = """
<!DOCTYPE html>
<html>
    <head>
        <title>Sign-up</title>
    </head>
</html>
"""

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            .error {{ color: red; }}
        
        </style>
    </head>  
    <body>
        
        <form method='post'>
        <form action='{{ url_for("/user-signup") }}'>

            <label for='username'>User Name:</label>
                <input type='text' name='username' placeholder="Username" required/> 
                    <p class='error'></p>
            
            <label for='password'>Password:</label>
                <input type='password' name='password' required/>
                    <p class='error'></p>     

            <label for='verify_password'>Verify password:</label>
                <input type='password' name='verify_password' required/>
                    <p class='error'></p>

            <label for='email'>Email (optional):</label>
                <input type='text' name='email' />     
                <p class ='error'></p>              
        
            <input type="submit" name='submit' value="Sign up" />

        </form>
    </body>          
</html>

"""
@app.route('/')
def index():
    error_message = request.args.get('error')
    return form.format(title = 'Sign up', error=error_message and cgi.escape(error_message, quote=True))

@app.route('/user-signup', methods=['POST'])
def user_signup():

    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']
    
    username_error = ''
    password_error = ''
    verify_password = ''
    email_error = ''
    email_regex = re.compile(r"[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+$")

    if username != username.isalnum():
        username_error = 'Invalid entry.  This field must contain between 3-20 alpha-numeric characters.'
    elif len(username) < 3 or len(username) > 20:
        username_error = 'Invalid entry.  This field must contain between 3-20 alpha-numeric characters.'


    if password != password.isalnum():
        password_error = 'Invalid entry.  This field must contain between 3-20 alpha-numeric characters.'
    elif len(password) < 3 or len(password) > 20:
        password_error = 'Invalid entry.  This field must contain between 3-20 alpha-numeric characters.'


    if verify_password != password.isalnum():
        verify_password_error = 'Your passwords do not match.'


    if not email_regex.match(email): 
        email_error = 'Invalid E-mail.'
    elif len(email) < 3 or len(email) > 20:
        email_error = 'Your email is outside the limits of 3 - 20 characters.'
    
    
    if not username_error and not password_error and not verify_password_error and not email_error:
        return redirect('/valid-form')   
    else:
        return render_template('index.html', username=username, username_error=username_error,
        password_error=password_error, verify_password_error=verify_password_error, email=email,
        email_error=email_error)        

    
@app.route('/valid-form', methods=['POST'])
def valid_form():
    username = request.form['username']
    return '<h1>Hello, '+ username +'. Thanks for submitting a wonderfully valid form.</h1>'

app.run()