from flask import Blueprint, jsonify, request
from App.controllers import (create_user, get_all_users_json)


user_views = Blueprint('user_views', __name__, template_folder='../templates')

@user_views.route('/api/users', methods=['GET'])
def get_users_action():
    users = get_all_users_json()
    return jsonify(users), 200

@user_views.route('/api/users', methods=['POST'])
def create_user_endpoint():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if not all([username, password]):
        return jsonify({"error": "Missing username or password"}), 400
    user = create_user(username, password)
    return jsonify({'message': f"user {user.username} created with id {user.id}"}), 201