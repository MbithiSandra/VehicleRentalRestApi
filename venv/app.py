from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory vehicle storage (simulating a database for simplicity)
vehicles = []

# Vehicle model
class Vehicle:
    def __init__(self, vehicle_id, name, description, price):
        self.id = vehicle_id
        self.name = name
        self.description = description
        self.price = price

    def to_dict(self):
        """Converts the vehicle object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price
        }

# Helper function to generate unique IDs
def generate_vehicle_id():
    return len(vehicles) + 1

# Root route
@app.route('/')
def welcome():
    return jsonify({
        'message': 'Welcome to the Vehicle Rental API!',
        'instructions': 'Use the /vehicles endpoint to interact with the API.'
    }), 200

# API Endpoint to POST (create) a new vehicle
@app.route('/vehicles', methods=['POST'])
def add_vehicle():
    data = request.get_json()  # Get the JSON data from the request body

    # Validate the required fields
    if not data.get('name') or not data.get('description') or not data.get('price'):
        return jsonify({'error': 'Missing required fields'}), 400

    # Generate a unique ID for the new vehicle
    vehicle_id = generate_vehicle_id()

    # Create a new vehicle object
    vehicle = Vehicle(vehicle_id, data['name'], data['description'], data['price'])

    # Add the vehicle to the vehicles list
    vehicles.append(vehicle)

    # Return a response indicating the vehicle was created
    return jsonify({'message': 'Vehicle added successfully', 'vehicle': vehicle.to_dict()}), 201

# API Endpoint to GET (retrieve) all vehicles
@app.route('/vehicles', methods=['GET'])
def get_vehicles():
    # Convert the list of vehicles into a list of dictionaries
    vehicles_list = [vehicle.to_dict() for vehicle in vehicles]

    # Return the list of vehicles as JSON
    return jsonify(vehicles_list), 200

if __name__ == '__main__':
    app.run(debug=True)
