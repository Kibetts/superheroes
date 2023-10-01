#!/usr/bin/env python
from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate
from wtforms import Form, StringField, validators

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

@app.route('/heroes/<int:hero_id>', methods=['GET'])  
def get_hero(hero_id):
  hero = Hero.query.get(hero_id)

  if hero:
    result = {}
    result['id'] = hero.id
    result['name'] = hero.name
    result['super_name'] = hero.super_name
    result['powers'] = []

    for power in hero.powers:
      power_data = {}
      power_data['id'] = power.id
      power_data['name'] = power.name
      power_data['description'] = power.description

      result['powers'].append(power_data)

    return jsonify(result)

  else:
    return jsonify({"error": "Hero not found"}), 404
  
@app.route('/powers', methods=['GET'])
def get_powers():
  powers = Power.query.all()
  result = []

  for power in powers:
    power_data = {}
    power_data['id'] = power.id
    power_data['name'] = power.name
    power_data['description'] = power.description

    result.append(power_data)

  return jsonify(result)

@app.route('/powers/<int:power_id>', methods=['GET'])
def get_power(power_id):
  power = Power.query.get(power_id)

  if power:
    result = {}
    result['id'] = power.id
    result['name'] = power.name
    result['description'] = power.description

    return jsonify(result)

  else:
    return jsonify({"error": "Power not found"}), 404
  

@app.route('/powers/<int:power_id>', methods=['PATCH'])
def update_power(power_id):
  data = request.get_json()

  if 'description' not in data:
    return jsonify({"error": "Description required"}), 400

  power = Power.query.get(power_id)

  if not power:
    return jsonify({"error": "Power not found"}), 404

  try:
    power.description = data['description']
    db.session.commit()
  except ValidationError as e:
    return jsonify({"errors": e.messages}), 400

  result = {}
  result['id'] = power.id
  result['name'] = power.name
  result['description'] = power.description

  return jsonify(result)




if __name__ == '__main__':
    app.run(port=5555)
