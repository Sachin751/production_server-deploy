from flask import render_template
from app import app

# Sample data for menu items
menu_items = [
    {"name": "Chai Latte", "price": "$3.50"},
    {"name": "Chai Ice Cream", "price": "$5.00"},
    {"name": "Chai Milkshake", "price": "$4.00"}
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html', menu_items=menu_items)

@app.route('/contact')
def contact():
    return render_template('contact.html')


