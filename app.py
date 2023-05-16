from flask import *
from model import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
app.debug = True

def logged_in(function):
    def decorated_function(*args, **kwargs):
        user_id = session.get('user_id')
        if not user_id:
            return redirect(url_for('login'))
        return function(*args,**kwargs)
    return decorated_function


@app.route('/')
def home():
    return render_template('home.html')
