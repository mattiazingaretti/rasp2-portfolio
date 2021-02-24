from flask import Flask, render_template, Blueprint


homeBp = Blueprint('home', __name__, template_folder="./templates")

@homeBp.route('/home')
def home():
    return render_template('Homedraft.html')



