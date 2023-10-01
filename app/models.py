from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Hero(db.Model):
    __tablename__ = 'hero'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80))
    super_name = db.Column(db.String(80))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def __init__(self, name, super_name):
        self.name = name
        self.super_name = super_name
    
class Power(db.Model):
    __tablename__ = 'powers'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80))
    description = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def __init__(self, name, description):
        self.name = name  
        self.description = description

    @validates('description')
    def validate_description(self, key, description):
        if not description or len(description) < 20:
          raise ValueError('Description must be present and at least 20 characters long.')
    
class HeroPower(db.Model):
    __tablename__ = 'hero_powers'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    strength = db.Column(db.String(80))
    hero_id = db.Column(db.Integer, db.ForeignKey('hero.id'))
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    hero = db.relationship('Hero', backref='hero_powers')
    power = db.relationship('Power', backref='hero_powers')

    def __init__(self, hero_id, power_id, strength):    
        self.hero_id = hero_id
        self.power_id = power_id
        self.strength = strength

    @validates('strength')
    def validate_strength(self, key, strength):
      if strength not in ['Strong', 'Weak', 'Average']:
        raise ValueError("Strength must be one of: 'Strong', 'Weak', 'Average'")

        

