from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, current_user, unset_jwt_cookies, decode_token, get_jwt_identity
from App.controllers import *

auth_views = Blueprint('auth_views', __name__, template_folder='../templates')

'''
Page/Action Routes
'''    

@auth_views.route('/api/identify', methods=['GET'])
@jwt_required()
def identify_user():
    user_id = get_jwt_identity()
    user = Driver.query.get(user_id)
    if user:
        role = "driver"
        extra = {
            "driver_name": user.driverName,
            "location": user.location,
            "status": user.status
        }
    else:
        user = Resident.query.get(user_id)
        if user:
            role = "resident"
            extra = {
                "resident_name": user.name,
                "street_id": user.streetId
            }
        else:
            return jsonify(error="User not found"), 404

    result = {
        "user_id": user.id,
        "username": user.username,
        "role": role
    }
    result.update(extra)
    return jsonify(result), 200
    
@auth_views.route('/api/login', methods=['POST'])
def login_action():
    data = request.json

    if not data or not data.get('username') or not data.get('password'):
        return jsonify({"error": "Username and password are required"}), 400

    token = jwt_authenticate(data['username'], data['password'])

    if not token:
        return jsonify({"error": "Bad username or password given"}), 401

    decoded_token = decode_token(token)
    user_identity = decoded_token['sub']   
    user_type = decoded_token.get('user_type')
    username = decoded_token.get('username')

    return jsonify({
        "access_token": token,
        "user_id": user_identity,
        "username": username,
        "user_type": user_type
    }), 200
    
@auth_views.route('/api/logout', methods=['GET'])
def logout_action():
    response = jsonify(message="Logged Out!")
    unset_jwt_cookies(response)
    return response
