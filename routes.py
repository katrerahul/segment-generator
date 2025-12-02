from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

from models import Segment, db
from app import app
from utils import generate


@app.route('/segment-generator', methods=['POST'])
def segment_generator():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'Missing text field'}), 400
    # segment = Segment(text=data['text'])
    # db.session.add(segment)
    # db.session.commit()
    segment_text = generate(data['text'])
    return jsonify({'segment_condition': segment_text})

