# hello_flask.py
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

# create an instance of Flask
app = Flask(__name__)

bootstrap = Bootstrap5(app)

# route decorator binds a function to a URL
@app.route('/')
def hello():
   return 'Hello world from Flask!'

# in hello_flask.py
@app.route('/mytemplate')
def t_test():
    return render_template('my_template_1.html')

@app.route('/pic')
def picture():
    # return "NOOOOOO"
    return render_template('index.html')

@app.route('/welcome')
def wc():
   s1 = 'Welcome to my page! '
   s2 = 'Have a nice day!'
   return s1 + s2

if __name__ == '__main__':
    app.run()