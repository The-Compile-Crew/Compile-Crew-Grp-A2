from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

driver_views = Blueprint('driver_views', __name__, template_folder='../templates')

@driver_views.route('/api/drivers', methods=['GET'])
@jwt_required()
def get_all_drivers():
    return jsonify({"message": "Will return all drivers soon"})

@driver_views.route('/api/drivers', methods=['POST'])
@jwt_required()
def create_driver():
    data = request.json
    return jsonify({"message": "Will create driver soon", "data": data}), 201

