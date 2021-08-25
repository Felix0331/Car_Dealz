
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user

class Car:
    def __init__(self, data):
        self.id = data['id']
        self.price = data['price']
        self.model = data['model']
        self.make = data['make']
        self.year = data['year']
        self.description = data['description']
        self.seller_name = data['seller_name']
        self.seller_id = data['seller_id']
        self.sold = data['sold']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @staticmethod
    def validate_car(car):
        is_valid = True
        if len(car['price']) == 0:
            flash("Must set a price higher than 0")
            is_valid = False
        elif int(car['price'])<=0:
            flash("Must set a price higher than 0")
            is_valid = False
        if len(car['model']) <= 0 :
            flash("Must provide vehicle name")
            is_valid = False
        if len(car['make']) <= 0:
            flash("Must provide make")
            is_valid = False
        if len(car['year']) <= 0:
            flash("Must provide year higher than 0")
            is_valid = False
        elif int(car['year'])<=0:
            flash("Must set a price higher than 0")
            is_valid = False
        if len(car['description']) <= 0:
            flash("must provide description")
            is_valid = False
        return is_valid

    @classmethod
    def add_car(cls,data):
        query = "INSERT INTO cars (price, model, make, year, description,seller_name,seller_id,sold,created_at, updated_at) VALUES (%(price)s,%(model)s,%(make)s,%(year)s,%(description)s,%(seller_name)s,%(seller_id)s,%(sold)s,NOW(),NOW());"
        return connectToMySQL('cars_db').query_db(query,data)
    @classmethod
    def edit_car(cls,data):
        query = "UPDATE cars SET price = %(price)s, model = %(model)s, make = %(make)s,year = %(year)s, description = %(description)s, updated_at = NOW() WHERE cars.id = %(id)s;"
        return connectToMySQL('cars_db').query_db(query,data)

    @classmethod
    def get_car(cls,data):
        query = "SELECT * FROM cars WHERE cars.id = %(id)s;"
        return connectToMySQL('cars_db').query_db(query,data)

    @classmethod
    def get_all_cars(cls):
        query = "SELECT * FROM cars;"
        cars = []
        results = connectToMySQL('cars_db').query_db(query)
        for car in results:
            cars.append(cls(car))
        return cars

    @classmethod
    def car_purchase(cls,data):
        query = "UPDATE cars SET sold = %(sold)s, updated_at = NOW() WHERE cars.id = %(id)s;"
        return connectToMySQL('cars_db').query_db(query,data)

    @classmethod
    def delete_car(cls,data):
        query = "DELETE FROM cars WHERE cars.id = %(id)s"
        return connectToMySQL('cars_db').query_db(query,data)



