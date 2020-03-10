"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
import seeds
import utils
from datetime import datetime, timedelta
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from flask_jwt_simple import JWTManager, create_jwt, jwt_required
from utils import APIException, generate_sitemap
from models import db, Users, Polls, Voters_Table, Chats
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
jwt = JWTManager(app)


######################################################################
# Takes in a dictionary with id, role and expiration date in minutes
#        create_jwt({ 'id': 100, 'role': 'admin', 'exp': 15 })
######################################################################
@jwt.jwt_data_loader
def add_claims_to_access_token(jkd):
    now = datetime.utcnow()
    kwargs = jkd if isinstance(jkd, dict) else {}
    id = kwargs.get('id')
    role = kwargs.get('role')
    exp = kwargs.get('exp', 365000)

    return {
        'exp': now + timedelta(days=exp),
        'iat': now,
        'nbf': now,
        'sub': id,
        'role': role
    }


@app.route('/temp_to_delete')
def jesus_issac():
    return jsonify( create_jwt() )


# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)



@app.route('/users', methods=['POST']) #register
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



@app.route('/users/token', methods=['POST']) #login
def handle_login():

    json = request.get_json()

    user = Users.query.filter_by(
        username = json['username'],
        password = utils.sha256(json['password'])
    ).first()

    if user is None:
        raise APIException('User Not Found: 404')

    return jsonify( create_jwt({}) )



@app.route('/seeds', methods=[ 'GET']) #clean tables
def seed(): 
    return seeds.run()



@app.route('/polls', methods=['GET']) #show all the polls
def get_polls():
    polls = Polls.query.all()
    return jsonify( [x.serialize() for x in polls] )


@app.route('/polls/<int:id>', methods=['GET']) #get a poll by id
def get_poll(id):
    poll = Polls.query.get(id)
    return jsonify( poll.serialize() )


@app.route('/polls/<int:user_id>', methods=['POST']) #make a poll
@jwt_required
def poll_maker(user_id):
    
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
        raise APIException(f'User not found: 404')

    db.session.add(Polls(
        poll_question = json['poll_question'],
        creator_user_id = user_id,
        poll_description = json['poll_description'],
        info_link = json['info_link'],
        image_link = json['image_link'],
        option1 = json['option1'],
        option2 = json['option2'],
        option3 = json['option3'],
        option4 = json['option4']
    ))
    db.session.commit()
    return jsonify(json)


@app.route('/vote', methods=['POST']) #vote
@jwt_required
def vote():

    json = request.get_json()

    voter = Users.query.filter_by(
        id = json['user_id']
    ).first()
    voting_on = Polls.query.filter_by(
        id = json['poll_id']
    ).first()

    v = Voters_Table(
        user_id = json['user_id'],
        poll_id = json['poll_id'],
        username = voter.username,
        poll_name = voting_on.poll_question,
        option_picked = json['option_picked']
    )
    db.session.add(v)
    db.session.commit()

    return f'{voter.username} voted in: {voting_on.poll_question}.'
    

@app.route('/chat', methods=['POST']) #add message to poll
def chat():
    json = request.get_json()

    post = Chats(
        poll_id = json["poll_id"],
        username = json["username"],
        message = json["message"]
    )
    db.session.add(post)
    db.session.commit()

    return 'added to chat'

@app.route('/chats/<int:id>')
def get_chats(id):

    chat = Chats.query.filter_by( chat_id=id ).order_by( Chats.created_at.asc() )

    return jsonify([a.serialize() for a in chat])

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
