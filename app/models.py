from core import db

#FIXME: Some database Columns may need meaningful defaults and onupdate callbacks.

jrnl_tags = db.Table('jrnl_tags',
db.Column('jrnl_id',db.Integer,db.ForeignKey('jrnl.id')),
db.Column('tag_id',db.Integer,db.ForeignKey('tag.id'))
)

class Jrnl(db.Model):
    """
    A tinyjrnl entry created by an end user
    """

    id = db.Column(db.Integer,primary_key=True)
    created_at = db.Column(db.DateTime,nullable=False)
    entry = db.Column(db.Text)
    channel_id = db.Column(db.Integer,db.ForeignKey('channel.id'))
    account_id = db.Column(db.String(34),db.ForeignKey('user.account_id'))
    tags = db.relationship('Tag',secondary=jrnl_tags,backref=db.backref('jrnls',lazy='dynamic'))

class Tag(db.Model):
    """
    A Tag applied to an Object, often Jrnl
    """
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255),unique=True)


class User(db.Model):
    """
    A tinyjrnl user
    """
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.Text,unique=True,nullable=False)
    password = db.Column(db.String(160),nullable=False)
    #TODO: Learn how to generate unique account_ids for users on sign up
    account_id = db.Column(db.String(34),nullable=False,unique=True) #FORMAT: AI[a-zA-Z0-9]{32}
    #TODO: Learn how to generate cryptographically secure api keys
    #TODO: Implement different authentication keys for different channels. This should be done before launch
    auth_key = db.Column(db.String(32),nullable=False) #FORMAT: [a-zA-Z0-9]{32}
    jrnls = db.relationship('Jrnl') # TODO: Investigate db.Column's onupdate and default values for usefulness


class Channel(db.Model):
    """
    A service that allows an end user send jrnl to tinyjrnl
    """
    #TODO: The data model for Channel may be incomplete. How am I going to handle storing authentication credentials and details for users' channels?
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255),nullable=False)
    code = db.Column(db.String(255),unique=True,nullable=False) #FORMAT [a-zA-Z0-9_] (alphanumeric)
    jrnls = db.relationship('Jrnl')
