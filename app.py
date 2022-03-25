from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource


app = Flask(__name__)

api = Api(app)

# create db
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///shop.db"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
db = SQLAlchemy(app)

# create users table
class Users(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    last_name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)  # verification of only one such email in db

db.create_all()



# creating a resource
class AddUser(Resource):

    def post(self):
        # get posted data
        posted_data = request.get_json()

        #add user to db
        new_user = Users(
            name=posted_data["name"],
            last_name=posted_data["last name"],
            email=posted_data["email"]
        )
        db.session.add(new_user)
        db.session.commit()
        return_map = {
            "status code": 200,
            "msg": "Successfuly added new user."
        }
        return jsonify(return_map)


api.add_resource(AddUser, "/add_user")



if __name__ == "__main__":
    app.run(debug=True)