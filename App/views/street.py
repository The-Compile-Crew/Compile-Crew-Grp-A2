from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from App.controllers.street_controller import create_street, get_all_streets, get_drives_by_street

street_views = Blueprint('street_views', __name__, template_folder='../templates')

@street_views.route('/api/streets', methods=['POST'])
@jwt_required()
def create_street_route():
    data = request.json
    name = data.get('name')
    if not name:
        return jsonify({"error": "Missing street name"}), 400
    street = create_street(name)
    return jsonify(street.get_json()), 201

@street_views.route('/api/streets', methods=['GET'])
@jwt_required()
def get_all_streets_route():
    streets = get_all_streets()
    return jsonify([s.get_json() for s in streets]), 200

@street_views.route('/api/streets/<street_id>/drives', methods=['GET'])
@jwt_required()
def get_drives_by_street_route(street_id):
    drives = get_drives_by_street(street_id)
    if drives is None:
        return jsonify({"error": "Street not found"}), 404
    return jsonify([d.get_json() for d in drives]), 200