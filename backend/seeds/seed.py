import bcrypt
from flask_seeder import Seeder, Faker
from src.models.user import User
from src.core import db




# All seeders inherit from Seeder
class DemoSeeder(Seeder):

  # run() will be called by Flask-Seeder
  def run(self):
    # Create a new Faker and tell it how to create User objects
    faker = Faker(
      cls=User,
      init={
        "name": "",
        "email": "",
        "password": "password"
      }
    )

    # Create 3 users
    names = ["shajalahamed","hello","go"]
    emails=["shajalahamedcse@gamil.com","hello@gmail.com","go@gmail.com"]
    counter = 0
    for user in faker.create(3):
        user.email=emails[counter]
        user.name=names[counter]
        # user.password= bcrypt.hashpw('password'.encode(), bcrypt.gensalt()).decode()
        counter+=1
        print("Adding user: %s" % user)
        self.db.session.add(user)