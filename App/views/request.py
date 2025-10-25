from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from App.controllers.request_controller import get_all_requests, get_requests_by_drive, create_request, update_request_status

request_views = Blueprint('request_views', __name__, template_folder='../templates')

@request_views.route('/api/requests', methods=['POST'])
@jwt_required()
def create_request_route():
    data = request.json
    resident_id = data.get('resident_id')
    drive_id = data.get('drive_id')

    if not all([resident_id, drive_id]):
        return jsonify({"error": "Missing resident_id or drive_id"}), 400
    request = create_request(resident_id, drive_id)

    if not request:
        return jsonify({"error": "Invalid resident or drive"}), 400
    return jsonify(request.get_json()), 201

@request_views.route('/api/view-requests', methods=['GET'])
@jwt_required()
def get_all_requests_route():
    requests = get_all_requests()
    return jsonify([r.get_json() for r in requests]), 200

@request_views.route('/api/requests/drive/<drive_id>', methods=['GET'])
@jwt_required()
def get_requests_by_drive_route(drive_id):
    requests = get_requests_by_drive(drive_id)
    return jsonify([r.get_json() for r in requests]), 200

@request_views.route('/api/requests/<request_id>/status', methods=['PUT'])
@jwt_required()
def update_request_status_route(request_id):
    data = request.json
    status = data.get('status')
    if not status:
        return jsonify({"error": "Missing status"}), 400
    request_obj = update_request_status(request_id, status)
    if not request_obj:
        return jsonify({"error": "Request not found"}), 404
    return jsonify(request_obj.get_json()), 200