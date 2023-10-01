from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Hero(db.Model):
    __tablename__ = 'hero'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    super_name = db.Column(db.String)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    
class Power(db.Model):
    __tablename__ = 'powers'

    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    
class HeroPower(db.Model):
    __tablename__ = 'hero_powers'

    id = db.Column(db.String, primary_key=True)
    strength = db.Column(db.Integer)
    hero_id = db.Column(db.String, db.ForeignKey('heroes.id'))
    power_id = db.Column(db.String, db.ForeignKey('powers.id'))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    hero = db.relationship('Hero', backref='hero_powers')
    power = db.relationship('Power', backref='hero_powers')

