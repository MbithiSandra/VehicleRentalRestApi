from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory vehicle storage (simulating a database for simplicity)
vehicles = []

# Vehicle model
class Vehicle:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def to_dict(self):
        """Converts the vehicle object to a dictionary."""
        return {
            'name': self.name,
            'description': self.description,
            'price': self.price
        }

# API Endpoint to POST (create) a new vehicle
@app.route('/vehicles', methods=['POST'])
def add_vehicle():
    data = request.get_json()  # Get the JSON data from the request body

    # Check if the required fields are in the incoming data
    if not data.get('name') or not data.get('description') or not data.get('price'):
        return jsonify({'error': 'Missing required fields'}), 400

    # Create a new vehicle object
    vehicle = Vehicle(name=data['name'], description=data['description'], price=data['price'])

    # Add the vehicle to the vehicles list (simulating saving to a database)
    vehicles.append(vehicle)

    # Return a response indicating the vehicle was created
    return jsonify({'message': 'Vehicle added successfully'}), 201

# API Endpoint to GET (retrieve) all vehicles
@app.route('/vehicles', methods=['GET'])
def get_vehicles():
    # Convert the list of vehicles into a list of dictionaries
    vehicles_list = [vehicle.to_dict() for vehicle in vehicles]

    # Return the list of vehicles as JSON
    return jsonify(vehicles_list), 200

if __name__ == '__main__':
    app.run(debug=True)
