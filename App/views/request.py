from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

request_views = Blueprint('request_views', __name__, template_folder='../templates')

@request_views.route('/api/requests', methods=['GET'])
@jwt_required()
def get_all_requests():
    return jsonify({"message": "Will return all requests soon"})

@request_views.route('/api/requests', methods=['POST'])
@jwt_required()
def create_request():
    data = request.json
    return jsonify({"message": "Will create request soon", "data": data}), 201
