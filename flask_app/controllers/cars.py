from flask import render_template,request,redirect,session,flash

from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.models.car import Car
from flask_app.models.user import User

@app.route('/dashboard')
def dashboard():
    if not session:
        flash("Please login")
        return redirect('/')
    cars = Car.get_all_cars()
    return render_template('dashboard.html',cars=cars)

@app.route('/add_car')
def add_car():
    if not session:
        flash("Please login")
        return redirect('/')
    return render_template('add_car.html')

@app.route('/create_new', methods = ['POST'])
def create_new():
    if not Car.validate_car(request.form):
        return redirect('/add_car')
    print(type(request.form['price']))
    print("&&&&&&&&&&&&&&&&&")
    data={
        'price':request.form['price'],
        'model':request.form['model'],
        'make':request.form['make'],
        'year':request.form['year'],
        'description':request.form['description'],
        'seller_name': session['name'],
        'seller_id': session['user_id'],
        'sold': 0
    }
    Car.add_car(data)
    return redirect('/dashboard')

@app.route('/edit/<int:car_id>')
def render_edit(car_id):
    if not session:
        flash("Please login")
        return redirect('/')
    data={
        'id': car_id
    }
    car = Car.get_car(data)
    return render_template('edit_car.html',car = car)

@app.route('/update/<int:car_id>', methods = ['POST'])
def update_car(car_id):
    if not session:
        flash("Please login")
        return redirect('/')
    if not Car.validate_car(request.form):
        return redirect(f'/edit/{car_id}')
    data={
        'id':car_id,
        'price':request.form['price'],
        'model':request.form['model'],
        'make':request.form['make'],
        'year':request.form['year'],
        'description':request.form['description'],
    }
    Car.edit_car(data)
    return redirect('/dashboard')

@app.route('/show/<int:car_id>')
def show_car(car_id):
    if not session:
        flash("Please login")
        return redirect('/')
    data={
        'id': car_id
    }
    car = Car.get_car(data)
    return render_template('show_car.html',car = car)

@app.route('/delete/<int:car_id>')
def delete_car(car_id):
    if not session:
        flash("Please login")
        return redirect('/')
    data = {
        'id':car_id
    }
    Car.delete_car(data)
    return redirect('/dashboard')
