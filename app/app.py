#!/usr/bin/env python
from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///heroes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return 'Welcome to superheroes arena'


@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    result = []

    for hero in heroes:
        hero_data = {}
        hero_data['id'] = hero.id
        hero_data['name'] = hero.name
        hero_data['super_name'] = hero.super_name

        result.append(hero_data)

    return jsonify(result)



if __name__ == '__main__':
    app.run(port=5555)
