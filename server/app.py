from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, User


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


migrate = Migrate(app, db)

db.init_app(app)


@app.route('/')
def index():
    host = request.headers.get('Host')
    return '<h1>Welcome to my tracker app!</h1>'

@app.route('/<string:username>')
def user(username):
    return f'<h1>Profile for {username}</h1>'

#add user
@app.route("/users", methods=["POST"])
def create_user():
    data = request.json
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")
    
    # new_user = User(username=data["username"])

    # Check if username, email, and password are provided
    if not username or not email or not password:
        return jsonify({"error": "Username, email, and password are required"}), 400

    # # Check if the username or email is already taken
    # existing_user = User.query.filter_by(username=username).first()
    # if existing_user:
    #     return jsonify({"error": "Username is already taken"}), 400

    # existing_email = User.query.filter_by(email=email).first()
    # if existing_email:
    #     return jsonify({"error": "Email is already registered"}), 400

    # Create a new user
    new_user = User(username=username, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()


    return jsonify({"Message": "User  created successfully"})

if __name__ == '__main__':
    app.run(port=5558 , debug = True)

    #debugger restarts the server and reload of the page