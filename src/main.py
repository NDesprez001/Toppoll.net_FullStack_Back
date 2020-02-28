"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
import seeds
import utils
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from flask_jwt_simple import JWTManager, create_jwt, jwt_required
from utils import APIException, generate_sitemap
from models import db, Users, Polls, Voters_Table
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
JWTManager(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/users', methods=['POST'])
def handle_register():

    json = request.get_json()

    property_check = ['first_name','last_name','username','password','date_of_birth','email']
    missing_props = []
    empty_props = []
    for prop in property_check:
        if prop not in json:
            missing_props.append(prop)
    if len(missing_props) > 0:
        raise APIException(f'Missing {", ".join(missing_props)} property in json')

    for prop in property_check:
        if json[prop] == "":
            empty_props.append(prop)
    if len(empty_props) > 0:
        raise APIException(f'Missing {", ".join(empty_props)} data in json')

    db.session.add(Users(
        first_name = json['first_name'],
        last_name = json['last_name'],
        username = json['username'],
        password = utils.sha256(json['password']),
        date_of_birth = json['date_of_birth'],
        email = json['email']
    ))
    db.session.commit()
    return jsonify(json)

@app.route('/users/token', methods=['POST'])
def handle_login():

    json = request.get_json()

    user = Users.query.filter_by(
        username = json['username'],
        password = utils.sha256(json['password'])
    ).first()

    if user is None:
        raise APIException('User Not Found: 404')

    return jsonify(create_jwt(identity=json['username']))

@app.route('/seeds', methods=[ 'GET'])
def seed():
    seeds.run()
    return 'seeds ran'


@app.route('/polls', methods=['GET'])
def get_polls():
    polls = Polls.query.all()
    list_of_polls = [{
        'id': i.id,
        'question': i.poll_question
    } for i in polls]
    return jsonify( list_of_polls )


@app.route('/polls/<int:id>', methods=['GET'])
def get_poll(id):
    poll = Polls.query.get(id)
    return jsonify( poll.serialize() )


@app.route('/polls/<int:user_id>', methods=['POST'])
@jwt_required
def poll_maker():
    
    json = request.get_json()

    property_check = ['poll_question','poll_description','option1','option2']
    missing_props = []
    empty_props = []
    for prop in property_check:
        if prop not in json:
            missing_props.append(prop)
    if len(missing_props) > 0:
        raise APIException(f'Missing {", ".join(missing_props)} property in json')

    for prop in property_check:
        if json[prop] == "":
            empty_props.append(prop)
    if len(empty_props) > 0:
        raise APIException(f'Missing {", ".join(empty_props)} data in json')

    client = Users.query.get(user_id)
    if client is None:
        raise APIException(f'User not found')

    db.session.add(Polls(
        poll_question = json['poll_question'],
        creator_user_id = user_id,
        poll_description = json['poll_description'],
        info_link = json['info_link'],
        option1 = json['option1'],
        option2 = json['option2'],
        option3 = json['option3'],
        option4 = json['option4']
    ))
    db.session.commit()
    return jsonify(json)

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
