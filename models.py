from flask_sqlalchemy import SQLAlchemy

from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///segments.db'
db: SQLAlchemy = SQLAlchemy(app)

class Segment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)
    segment_condition = db.Column(db.String, nullable=False)
