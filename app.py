from flask import Flask, request, jsonify, abort
from .config import ProductionConfig, DevelopmentConfig
from .repo import create_repository

app = Flask(__name__)
#app.config['ENV'] = 'development'

if app.config['ENV'] == 'production':
    app.config.from_object(ProductionConfig)
else:
    app.config.from_object(DevelopmentConfig)

repository = create_repository(app)


@app.route('/toys', methods=['GET'])
def get_toys():
    toys = repository.get_toys()
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 5))
    search_name = request.args.get('name', '').lower()

    if search_name:
        filtered_toys = [toy for toy in toys if search_name in toy.name.lower()]
    else:
        filtered_toys = toys

    start_idx = (page - 1) * per_page
    end_idx = start_idx + per_page

    toys_on_page = filtered_toys[start_idx:end_idx]
    toys = [t.to_dict() for t in toys_on_page]
    return jsonify({"toys": toys, "page": page, "per_page": per_page, "total_items": len(filtered_toys)})


@app.route('/toys', methods=['POST'])
def add_toy():
    new_toy = request.json
    repository.add_toy(new_toy)
    return jsonify({"message": "Toy added successfully", "toy": new_toy}), 201


@app.route('/toys/<int:toy_id>', methods=['PUT'])
def update_toy(toy_id):
    updated_toy_data = request.json
    updated_toy = repository.update_toy(toy_id, updated_toy_data)
    if updated_toy is None:
        abort(404, description="Toy not found")
    else:
        return jsonify({"message": "Toy updated successfully",
                        "toy": {"id": updated_toy.id, "name": updated_toy.name}})


@app.route('/toys/<int:toy_id>', methods=['DELETE'])
def delete_toy(toy_id):
    deleted_toy = repository.delete_toy(toy_id)
    if deleted_toy is not None:
        return jsonify({"message": "Toy deleted successfully"})
    else:
        abort(404, description="Toy not found")


@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad request"}), 400


# @app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
