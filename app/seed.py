from app import app 
from models import *
import random

print("🦸‍♀️ Seeding powers...")
powers_data = [
    {"name": "super strength", "description": "gives the wielder super-human strengths"},
    {"name": "flight", "description": "gives the wielder the ability to fly through the skies at supersonic speed"},
    {"name": "super human senses", "description": "allows the wielder to use her senses at a super-human level"},
    {"name": "elasticity", "description": "can stretch the human body to extreme lengths"}
]

with app.app_context():
    for power_info in powers_data:
      power = Power(**power_info)
      db.session.add(power)

    db.session.commit()


print("🦸‍♀️ Seeding heroes...")
heroes_data = [
    {"name": "Kamala Khan", "super_name": "Ms. Marvel"},
    {"name": "Doreen Green", "super_name": "Squirrel Girl"},
    {"name": "Gwen Stacy", "super_name": "Spider-Gwen"},
    {"name": "Janet Van Dyne", "super_name": "The Wasp"},
    {"name": "Wanda Maximoff", "super_name": "Scarlet Witch"},
    {"name": "Carol Danvers", "super_name": "Captain Marvel"},
    {"name": "Jean Grey", "super_name": "Dark Phoenix"},
    {"name": "Ororo Munroe", "super_name": "Storm"},
    {"name": "Kitty Pryde", "super_name": "Shadowcat"},
    {"name": "Elektra Natchios", "super_name": "Elektra"}
]

with app.app_context():
  for hero_info in heroes_data:
      hero = Hero(**hero_info)
      db.session.add(hero)

  db.session.commit()

print("🦸‍♀️ Adding powers to heroes...")
strengths = ["Strong", "Weak", "Average"]
heroes = Hero.query.all()

with app.app_context():
  for hero in heroes:
      for _ in range(random.randint(1, 3)):
          power = random.choice(Power.query.all())
          hero_power = HeroPower(hero_id=hero.id, power_id=power.id, strength=random.choice(strengths))
          db.session.add(hero_power)

  db.session.commit()
  
print("🦸‍♀️ Done seeding!")
