from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from App.controllers.resident_controller import create_resident, view_my_requests

resident_views = Blueprint('resident_views', __name__, template_folder='../templates')

@resident_views.route('/api/residents', methods=['POST'])
@jwt_required()
def create_resident_route():
    data = request.json
    name = data.get('name')
    street_id = data.get('street_id')

    if not all([name, street_id]):
        return jsonify({"error": "Missing name or street_id"}), 400
    
    resident = create_resident(name, street_id)
    return jsonify(resident.get_json()), 201

@resident_views.route('/api/residents/<resident_id>/requests', methods=['GET'])
@jwt_required()
def get_resident_requests_route(resident_id):
    requests = view_my_requests(resident_id)
    if requests is None:
        return jsonify({"error": "Resident not found"}), 404
    return jsonify([r.get_json() for r in requests]), 200