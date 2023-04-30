from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Ejemplo de datos en memoria
products = [
    {'id': 1, 'name': 'Producto 1', 'price': 10.99},
    {'id': 2, 'name': 'Producto 2', 'price': 19.99},
    {'id': 3, 'name': 'Producto 3', 'price': 5.99},
]

# Obtener una lista de todos los productos
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

# Obtener un producto por ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = [product for product in products if product['id'] == product_id]
    if len(product) == 0:
        abort(404)
    return jsonify(product[0])

# Crear un nuevo producto
@app.route('/products', methods=['POST'])
def create_product():
    if not request.json or not 'name' in request.json:
        abort(400)
    product = {
        'id': products[-1]['id'] + 1,
        'name': request.json['name'],
        'price': request.json.get('price', 0.0),
    }
    products.append(product)
    return jsonify(product), 201

# Actualizar un producto existente
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = [product for product in products if product['id'] == product_id]
    if len(product) == 0:
        abort(404)
    if not request.json:
        abort(400)
    product[0]['name'] = request.json.get('name', product[0]['name'])
    product[0]['price'] = request.json.get('price', product[0]['price'])
    return jsonify(product[0])

# Eliminar un producto existente
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = [product for product in products if product['id'] == product_id]
    if len(product) == 0:
        abort(404)
    products.remove(product[0])
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)
