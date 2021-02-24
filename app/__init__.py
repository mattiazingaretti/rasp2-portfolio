from flask import Flask, redirect, url_for
from home.routers import homeBp

app = Flask(__name__ ,static_folder='./static')

app.register_blueprint(homeBp)

@app.route('/')
def index():
   return redirect(url_for('home.home'))