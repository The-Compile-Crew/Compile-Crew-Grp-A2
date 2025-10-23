from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

resident_views = Blueprint('resident_views', __name__, template_folder='../templates')

@resident_views.route('/api/residents', methods=['GET'])
@jwt_required()
def get_all_residents():
    return jsonify({"message": "Will return all residents soon"})

@resident_views.route('/api/residents', methods=['POST'])
@jwt_required()
def create_resident():
    data = request.json
    return jsonify({"message": "Will create resident soon", "data": data}), 201

@resident_views.route('/api/residents/<int:resident_id>', methods=['GET'])
@jwt_required()
def get_resident(resident_id):
    return jsonify({"message": f"Will get resident {resident_id} soon"})