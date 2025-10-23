from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

street_views = Blueprint('street_views', __name__, template_folder='../templates')

@street_views.route('/api/streets', methods=['GET'])
@jwt_required()
def get_all_streets():
    return jsonify({"message": "Will return all streets soon"})

@street_views.route('/api/streets', methods=['POST'])
@jwt_required()
def create_street():
    data = request.json
    return jsonify({"message": "Will create street soon", "data": data}), 201

@street_views.route('/api/streets/<int:street_id>', methods=['GET'])
@jwt_required()
def get_street(street_id):
    return jsonify({"message": f"Will get street {street_id} soon"})