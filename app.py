from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'b88b38f6008d6792596f4bfb89e8ba04'
posts = [

{
    'author' : 'amr',
    'title' : 'blog Post1',
    'content' : 'first post',
    'date_posted' : 'today'
},

{
    'author' : 'ahmed',
    'title' : 'blog Post2',
    'content' : 'second post',
    'date_posted' : 'yesterday'
}

]

@app.route('/')


@app.route('/about')
def about():
    return render_template('about.html', title = 'about')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html', title = 'register' , form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title = 'login' , form=form)
if __name__ == "__main__":
    app.run(debug=True)