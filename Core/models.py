from dataclasses import dataclass
from Core.database import db


@dataclass
class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))

    name: str
    email: str
    password: str

    def get_id(self):
        return self.id

    def __repr__(self):
        return f"<User {self.name}>"


@dataclass
class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.String(100))

    title: str
    content: str

    def __repr__(self):
        return f'<Post {self.title}>'


@dataclass
class Videos(db.Model):
    __tablename__ = 'videos'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.String(100))
    source = db.Column(db.String(100))

    title: str
    content: str
    source: str

    def __repr__(self):
        return f'<Video {self.title}>'
