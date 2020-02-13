from flask import Flask, jsonify, request
from products import products

app = Flask(__name__)  # aplicación de Flask

"""Entregar datos
Creación de rutas para servir datos (productos)
Características:
    - Permiten especificar los métodos HTTP
"""


@app.route('/ping')
def index():
    return jsonify({"message": "ruta de prueba"})


# Por defecto, las rutas manejan petición GET
@app.route('/products', methods=['GET'])
def getProducts():
    # return jsonify(products)
    return jsonify({"products": products})  # Propiedad products


# Mostrar producto en particular
# @app.route('/priducts/<string:product_name>')
@app.route('/products/<product_name>')
def getProduct(product_name):
    productsFound = [product for product in products
        if product['name'] == product_name]
    if (len(productsFound) > 0):
        return jsonify({"product": productsFound[0]})
    return jsonify({"message": "Product not found"})


# Ruta para crear datos
@app.route('/products', methods=['POST'])
def addProduct():
    new_product = {
        "name": request.json["name"],
        "price": request.json["price"],
        "quantity": request.json["quantity"]
    }
    products.append(new_product)
    return jsonify({"message": "Product Added Successfully", "products": products})


# Ruta para actualizar un producto
@app.route('/products/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if (len(productFound) > 0):
        productFound[0]['name'] = request.json['name']
        productFound[0]['price'] = request.json['price']
        productFound[0]['quantity'] = request.json['quantity']

        return jsonify({"message": "Product Updated", "product": productFound[0]})
    return jsonify({"message": "Product not found"})


if __name__ == '__main__':
    app.run(debug=True, port=9091)  # Inicialización de la aplicación
