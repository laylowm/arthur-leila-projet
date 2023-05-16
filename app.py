from flask import *
from model import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
app.debug = True

def 

@app.route('/')
def home():
