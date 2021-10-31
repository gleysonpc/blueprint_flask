from flask import Blueprint, jsonify, request

products_bp = Blueprint('products_bp', __name__)

@products_bp.route('', methods=['GET'])
def index():
    return jsonify({'message': 'list all products'})

@products_bp.route('', methods=['POST'])
def create():
    body = request.get_json()
    name = body.get('name')
    price = body.get('price')    
    return jsonify({'message': {'name': name, 'price':price}})