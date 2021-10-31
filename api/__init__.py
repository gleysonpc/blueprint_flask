from flask import Flask
from flask_cors import CORS
from .products import products_bp

def create_app():
    app = Flask(__name__)
    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'  
    app.register_blueprint(products_bp, url_prefix='/products')

    return app

# if __name__ == '__main__':
#     app.run(host='0.0.0.0')

