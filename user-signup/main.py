from flask import Flask, request, redirect, render_template
import cgi
import re


app = Flask(__name__)
app.config['DEBUG'] = True

#page_header = """
#<!DOCTYPE html>
#<html>
 #   <head>
  #      <title>Sign-up</title>
   # </head>
#</html>
#"""
#        <form action='{{ url_for("/user-signup") }}'>




@app.route('/')
def index():

    return render_template('user-signup.html')
 #   error = request.args.get('error')
  #  if request.method == 'POST':
   #     username = request.form['username']
    #    password = request.form['password']
     #   verify_password = request.form['verify_password']
      #  email = request.form['email']

     
   
   #return form.format(title = 'Sign up', error=error and cgi.escape(error, quote=True))


@app.route('/', methods=['POST'])
def user_signup():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']
    
    username_error = ''
    password_error = ''
    verify_password_error = ''
    email_error = ''
    email_regex = re.compile(r"[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+$")

   
    if (len(username) < 3 or len(username) > 20) or (" " in username):
        
        username_error = 'Invalid entry.  This field must contain between 3-20 alpha-numeric characters.'
        username = ''

    if len(password) < 3 or len(password) > 20:
        password_error = 'Invalid entry.  This field must contain between 3-20 alpha-numeric characters.'
        password = ''

    if verify_password != password:
        verify_password_error = 'Your passwords do not match.'
        verify_password = ''

    if not email_regex.match(email): 
        email_error = 'Invalid E-mail.'
    if email != '' and (len(email) < 3 or len(email) > 20):
        email_error = 'Your email is outside the limits of 3 - 20 characters.'
    
    
    if not username_error and not password_error and not verify_password_error and not email_error:
        user = username
        return redirect('/welcome?user={0}'.format(user))   
    else:
        return render_template('user-signup.html', username_error=username_error,
        password_error=password_error, verify_password_error=verify_password_error,
        email_error=email_error, username=username, password=password, verify_password=verify_password, email=email, )        

    
@app.route('/welcome', methods=['POST', 'GET'])
def welcome():
   # username = request.form['username']
    user = request.args.get('user')
    
    return render_template('valid-form.html', user=user)
    #return #'<h1>Hello, '+ username +'. Thanks for submitting a wonderfully valid form.</h1>'

app.run()