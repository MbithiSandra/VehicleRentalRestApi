from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database (for simplicity, will be replaced by real DB in future)
vehicles = []

# Endpoint to add a new vehicle
@app.route('/vehicles', methods=['POST'])
def create_vehicle():
    data = request.get_json()

    # Validate input
    if not data or 'name' not in data or 'description' not in data or 'price' not in data:
        return jsonify({'error': 'Bad Request', 'message': 'Missing required fields'}), 400

    # Create a new vehicle and add to the list
    vehicle = {
        'name': data['name'],
        'description': data['description'],
        'price': data['price']
    }
    vehicles.append(vehicle)
    
    return jsonify(vehicle), 201  # Return the created vehicle with a 201 status

# Endpoint to get the list of all vehicles
@app.route('/vehicles', methods=['GET'])
def get_vehicles():
    return jsonify(vehicles)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
