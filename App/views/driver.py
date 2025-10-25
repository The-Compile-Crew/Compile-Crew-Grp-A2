from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from App.controllers.driver_controller import create_driver, get_requests_by_driver, schedule_drive, update_driver_location, update_driver_status


driver_views = Blueprint('driver_views', __name__, template_folder='../templates')

@driver_views.route('/api/drivers', methods=['POST'])
@jwt_required()
def create_driver_route():
    data = request.json
    username = data.get('username')
    driverName = data.get('driverName')
    password = data.get('password')
    location = data.get('location')
    status = data.get('status', 'available')

    if not all([username, driverName, password, location]):
        return jsonify({"error": "Missing required fields"}), 400
    
    driver = create_driver(username, driverName, password, location, status)
    return jsonify(driver.get_json()), 201

@driver_views.route('/api/drivers/<driver_id>/location', methods=['PUT'])
@jwt_required()
def update_location_route(driver_id):
    data = request.json
    location = data.get('location')
    if not location:
        return jsonify({"error": "Missing location"}), 400
    driver = update_driver_location(driver_id, location)
    if not driver:
        return jsonify({"error": "Driver not found"}), 404
    return jsonify(driver.get_json()), 200

@driver_views.route('/api/drivers/<driver_id>/status', methods=['PUT'])
@jwt_required()
def update_status_route(driver_id):
    data = request.json
    status = data.get('status')
    if not status:
        return jsonify({"error": "Missing status"}), 400
    driver = update_driver_status(driver_id, status)
    if not driver:
        return jsonify({"error": "Driver not found"}), 404
    return jsonify(driver.get_json()), 200

@driver_views.route('/api/drivers/<driver_id>/drives', methods=['POST'])
@jwt_required()
def schedule_drive_route(driver_id):
    data = request.json
    street_id = data.get('street_id')
    scheduled_time = data.get('scheduled_time')
    if not all([street_id, scheduled_time]):
        return jsonify({"error": "Missing street_id or scheduled_time"}), 400
    drive = schedule_drive(driver_id, street_id, scheduled_time)
    return jsonify(drive.get_json()), 201

@driver_views.route('/api/drivers/<driver_id>/requests', methods=['GET'])
@jwt_required()
def get_requests_route(driver_id):
    requests = get_requests_by_driver(driver_id)
    return jsonify([r.get_json() for r in requests]), 200
