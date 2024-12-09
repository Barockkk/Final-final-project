from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///resources.db'
db = SQLAlchemy(app)

# Models
class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    category = db.Column(db.String(50))
    location = db.Column(db.String(200))
    occupancy = db.Column(db.Integer, default=0)

# Routes
@app.route('/resources', methods=['GET'])
def get_resources():
    resources = Resource.query.all()
    return jsonify([{
        'id': r.id,
        'name': r.name,
        'category': r.category,
        'location': r.location,
        'occupancy': r.occupancy
    } for r in resources])

@app.route('/resources', methods=['POST'])
def add_resource():
    data = request.json
    new_resource = Resource(
        name=data['name'],
        category=data['category'],
        location=data['location'],
        occupancy=data['occupancy']
    )
    db.session.add(new_resource)
    db.session.commit()
    return jsonify({'message': 'Resource added successfully'}), 201

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
    print("hello world")