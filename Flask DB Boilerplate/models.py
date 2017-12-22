from app import db
from sqlalchemy.dialects.postgresql import JSON


class Equation(db.Model):
    __tablename__ = 'equation'
    
    id = db.Column(db.Integer, primary_key=True)
    
    equation = db.Column(db.String(), unique=True)
    words = db.Column(db.String())
    promotedwords = db.Column(db.String())
    access_times = db.Column(db.String())

    def __init__(self, equation, words, promotedwords, access_times):
        self.equation = equation
        self.words = words
        self.promotedwords = promotedwords
        self.access_times = access_times

    def __repr__(self):
        return '<Equation: {}, Words: {}>'.format(self.equation, self.words)


class Word(db.Model):
    __tablename__ = 'word'
    
    id = db.Column(db.Integer, primary_key=True)
    
    word = db.Column(db.String(), unique=True)
    embedding = db.Column(db.String())

    def __init__(self, word, embedding):
        self.word = word
        self.embedding = embedding

    def __repr__(self):
        return '<Word: {}, Embedding: {}>'.format(self.word, self.embedding)
