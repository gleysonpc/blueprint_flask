from flask import Flask
from users import users_bp
from products import products_bp

app = Flask(__name__)
app.register_blueprint(users_bp, url_prefix='/users')
app.register_blueprint(products_bp, url_prefix='/products')

if __name__ == '__main__':
    app.run(debug=True)