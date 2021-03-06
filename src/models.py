from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(40))
    last_name = db.Column(db.String(40))
    username = db.Column(db.String(40), unique=True)
    password = db.Column(db.String(70))
    date_of_birth = db.Column(db.String(10))
    email = db.Column(db.String(120))


    polls_created = db.relationship('Polls', back_populates='creator_user')
    votes = db.relationship('Voters_Table', back_populates='user')

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "username": self.username,
            "date of birth": self.date_of_birth,
            "email": self.email,
            "polls_created": [b.serialize() for b in self.polls_created]
        }



class Polls(db.Model):
    __tablename__ = 'polls'
    id = db.Column(db.Integer, primary_key=True)
    creator_user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    poll_question = db.Column(db.String(100))
    poll_description = db.Column(db.String(500))
    info_link = db.Column(db.String(200))
    image_link = db.Column(db.String(600))
    date_started = db.Column(db.DateTime, default=datetime.utcnow)
    
    option1 = db.Column(db.String(150), nullable=False)
    option2 = db.Column(db.String(150), nullable=False)
    option3 = db.Column(db.String(150), default=None)
    option4 = db.Column(db.String(150), default=None)

    creator_user = db.relationship('Users', back_populates='polls_created')
    votes = db.relationship('Voters_Table', back_populates='poll')
    chat = db.relationship('Chats', back_populates='poll')

    def calculate_vote_percentages(self):  #finds the percentages of the votes
        if len(self.votes) == 0:
            return {}
        options = ['option1','option2','option3','option4']
        count = {}
        for option in options:
            attr = getattr(self, option)
            if attr is not None:
                count[ attr ] = 0
        for vote in self.votes:
            count[ vote.option_picked ] += 1
        for option, numb in count.items():
            count[option] = float(numb)/len(self.votes)*100

        return count


    def __repr__(self):
        return '<Polls %r>' % self.poll_question

    def serialize(self):
        return {
            "id": self.id,
            "poll_question": self.poll_question,
            "poll_description": self.poll_description,
            "date_started" : self.date_started,
            "info_link" : self.info_link,
            "image_link" : self.image_link,
            "creator_user": self.creator_user.username,
            "option1" : self.option1,
            "option2" : self.option2,
            "option3" : self.option3,
            "option4" : self.option4,
            "percentages": self.calculate_vote_percentages(),
            "voting_users" : [a.serialize() for a in self.votes],
            "chat" : [b.serialize() for b in self.chat]
        }

class Voters_Table(db.Model):
    __tablename__ = 'voters_table'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    username = db.Column(db.String(40))
    poll_id = db.Column(db.Integer, db.ForeignKey('polls.id'))
    poll_name = db.Column(db.String(100))
    option_picked = db.Column(db.String(150), nullable=False)

    user = db.relationship('Users', back_populates='votes')
    poll = db.relationship('Polls', back_populates='votes')
    

    def __repr__(self):
        return '<Voters_Table %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user_id" : self.user_id,
            "username": self.user.username,
            "poll_id" : self.poll_id,
            "poll_name" : self.poll.poll_question,
            "option_picked" : self.option_picked
            # "my_name": "issac",
            # "understand you can put anything here": self.user.password,
            # "user dob": self.user.date_of_birth,
            # "poll_data": self.poll.poll_description,
            # "more poll": self.poll.poll_question
        }



class Chats(db.Model):
    __tablename__ = 'chats'
    id = db.Column(db.Integer, primary_key=True)
    poll_id = db.Column(db.Integer, db.ForeignKey('polls.id'))
    username = db.Column(db.String(40))
    message = db.Column(db.String(1000))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    poll = db.relationship('Polls', back_populates='chat')
    
    # def __init__(self, chat_id, username, message, created_at):
    #     print(self.chat)
    #     self.poll_id = poll_id
    #     self.writer_username = username
    #     self.message = message
    #     self.created_at = created_at

    def __repr__(self):
        return '<Chat %r>' % self.id

    def serialize(self):
        return {
            "username": self.username,
            "message": self.message,
            "created_at": self.created_at
        }


# class Person(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)

#     def __repr__(self):
#         return '<Person %r>' % self.username

#     def serialize(self):
#         return {
#             "username": self.username,
#             "email": self.email
#         }