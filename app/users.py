from flask import Blueprint, jsonify

users_bp = Blueprint('users_bp', __name__)

@users_bp.route('', methods=['GET'])
def index():
    return jsonify({'message': 'list all users'})

@users_bp.route('', methods=['POST'])
def create():
    return jsonify({'message': 'create a new user'})