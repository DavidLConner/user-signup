from flask import Flask, request, redirect, render_template
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

user_signup_form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            .error {{ color: red; }}
        
        </style>
    </head>  
    <body>
        
        <form method='post'>
        <form action ='/user'>

            <label for='username'>User Name:</label>
                <input type='text' name='username'> 
                    <p class='error'>{username_error}</p>
            
            <label for='password'>Password:</label>
                <input type='password' name='password' value={password}>
                    <p class='error'>{password_error}</p>     

            <label for='verify_password'>Verify password:</label>
                <input type='password' name='verify_password'>
                    <p class='error'>{verify_password_error}</p>

            <label for='email'>Email (optional):</label>
                <input type='text' name='email' value={email}>     
                <p class ='error'>{email_error}</p>              


           
            <input type="submit" value="Validate" />

        </form>
    </body>          
</html>

"""

@app.route('/user-signup')
def signup_form():
    return user_signup_form.format(username='', username_error='', password='',
    password_error='', verify_password='', verify_password_error='', email='', email_error='')



@app.route('/user-signup', methods=['POST'])
def validation():
   
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']
    
    username = ''
    password = ''
    verify_password == password
    email = ''
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
    
    else:
        if not username_error and not password_error and not verify_password_error and not email_error:
            return redirect('/valid_form')           

    
@app.route('/valid_form', methods=['POST'])
def valid_form():
    username = request.form['username']
    return '<h1>Hello, '+ username +'. Thanks for submitting a wonderfully valid form.</h1>'

app.run()