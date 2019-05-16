from flask import Flask, redirect, url_for
app = Flask(__name__)

#url_for()


# @app.route('/')
# def index():
#     return 'Hello, Flask!'

# GET By defual 
# POST  Hide 
# HEAD 
# PUT
# DELEte

# @app.route('/')
# def index():
#    return '<html><body> <h1> Hello WOrld </h1></body>  </html>'

# @app.route('/admin')
# def hello_admin():
#    return 'Hello Admin'

# @app.route('/guest/<guest>')
# def hello_guest(guest):
#    return 'Hello %s as Guest' % guest

# @app.route('/user/<name>')
# def hello_user(name):
#    if name =='admin':
#       return redirect(url_for('hello_admin'))
#    else:
#       return redirect(url_for('hello_guest',guest = name))

@app.route('/')
def index():
   return '<html><body> <h1> Hello WOrld Zeshna  </h1></body>  </html>'


   

if __name__ == '__main__':
   app.run(debug = True)