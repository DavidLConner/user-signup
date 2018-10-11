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
                <input type='password' name='Verify_password'>
                    <p class='error'>{verify_password_error}</p>

            <label for='email'>Email (optional):</label>
                <input type='email' name='E-mail' value={email}>     
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
    verify_password = ''
    email = ''
    email_regex = re.compile(r"[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+$")

    
    if len(username) < 3 or len(username) > 20:
        username_error = 'Invalid entry.  This field must contain between 3-20 alpha-numeric characters.'
        return render_template(username=username, email=email, name_error=username_error)
    
    if username.isalnum() and password == verify_password and len(email) > 20:
        email_error = 'Invalid entry.  This field must contain between 3-20 alpha-numeric characters.'
        return render_template(username=username, email=email, email_error=email_error)
    
    if username.isalnum() and password == verify_password and len(password) > 20:
        password_error = 'Invalid entry.  This field must contain between 3-20 alpha-numeric characters.'
        return render_template(username=username, email=email, password_error=password_error )
    
    if username.isalnum() and password == verify_password and len(password) < 3:
        password_error = 'Invalid entry.  This field must contain between 3-20 alpha-numeric characters.'
        return render_template(username=username, email=email, password_error=password_error)     
    
    if username.isalnum() and password == verify_password and len(verify_password) > 20:
        password_error = 'Invalid entry.  This field must contain between 3-20 alpha-numeric characters.'
        return render_template(username=username, email=email, password_error=password_error )
    
    if username.isalnum() and password == verify_password and len(verify_password) < 3:
        password_error = 'Invalid entry.  This field must contain between 3-20 alpha-numeric characters.'
        return render_template(username=username, email=email, password_error=password_error)     
     
    
    if username.isalnum() and password == verify_password and len(email) < 3:
        email_error = 'Invalid entry.  This field must contain between 3-20 alpha-numeric characters.'
        return render_template(username=username, email=email, email_error=email_error)  

    if username.isalnum() and password == verify_password and len(email):
        if not email_regex.match(email): 
            email_error = 'Invalid E-mail.'
            return render_template(username=username, email=email, email_error=email_error)
        if email_regex.match(email):
            return render_template('/valid_form')

    if username.isalnum() and password != verify_password:
        password_error = 'The passwords do not match.'
        return render_template(username=username, email=email, password_error=password_error)
    else:
        username_error = 'Invalid entry.  This field must contain between 3-20 alpha-numeric characters.'
        return render_template(username=username, email=email, username_error=username_error)
    
@app.route('/valid_form', methods=['POST'])
def valid_form():
    username = request.form['username']
    return '<h1>Hello, ' + username +'. Thanks for submitting a wonderfully valid form.</h1>'

app.run()