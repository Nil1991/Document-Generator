import flask, json, flask_sqlalchemy
from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base


#Conecting to the database
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/school'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100))

    def to_json(self):
        return {"id": self.id, "name": self.name, "email": self.email}


#Select all
@app.route("/users", methods=["GET"])
def select_usuarios():
    users_class = User.query.all()
    users_json = [user.to_json() for user in users_class]
    print(users_json)
    return Response(json.dumps(users_json))
print('wrong')
#Single select
#Create 
#Update
#Delete



app.run()



