from buckeT import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
# from itsdangerous import (TimedJSONWebSignatureSerializer
                        #   as Serializer, BadSignature, SignatureExpired)


class User(db.Model):
    """Creating the users table. This table will hold all users in the system."""
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String, nullable=False)
    second_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password_hash = db.Column(db.String, nullable=False, unique=True)
    bucketlists = db.relationship('BucketList', backref='bucketlists', lazy='dynamic',
                                  cascade="all, delete-orphan")

    @property
    def password(self):
        """Show an error message when a user tries to edit the password
        field in the database.
        """
        raise AttributeError('Password field is a write-only field, can not be changed!')

    @password.setter
    def password(self, password):
        """Creates a hashed password."""
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """Compare password hashes with that saved in the user table."""
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.email)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def get_all(self):
        return User.query.all()


class BucketList(db.Model):
    """creating the bucketlists table. This table will hold all
    bucket lists created.
    """
    __tablename__ = 'bucketlists'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False, unique=True)
    date_created = db.Column(db.DateTime, default=db.func.now())
    date_modified = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
    created_by = db.Column(db.String, db.ForeignKey('Users.email'))
    bucketlist_items = db.relationship('BucketListItem', backref='items', lazy='dynamic',
                                     cascade="all, delete-orphan")

    def __init__(self, name, user_email):
        self.name = name
        self.created_by = user_email

    def __repr__(self):
        return '<BucketList {}>'.format(self.name)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def get_all(self):
        return Bucketlist.query.all()


class BucketListItem(db.Model):
    """Creating the Bucketlist Items table. This table will hold all
    items in all bucket lists.
    """
    __tablename__ = 'Bucketlist Items'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    date_created = db.Column(db.DateTime, default=db.func.now())
    date_modified = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
    bucket_list_it_belongs_to = db.Column(db.String, db.ForeignKey('bucketlists.name'))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Bucket_list_Item {}>'.format(self.name)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def get_all(self):
        return BucketListItem.query.all()

