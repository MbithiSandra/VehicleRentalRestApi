import requests
import json

BASE_URL = 'http://127.0.0.1:5000/vehicles'

# Function to add a new vehicle
def add_vehicle(name, description, price):
    vehicle_data = {
        'name': name,
        'description': description,
        'price': price
    }
    
    response = requests.post(BASE_URL, json=vehicle_data)
    
    if response.status_code == 201:
        print("Vehicle added successfully:", response.json())
    else:
        print("Error:", response.status_code, response.json())

# Function to get all vehicles
def get_vehicles():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        vehicles = response.json()
        print("List of Vehicles:")
        for vehicle in vehicles:
            print(f"Name: {vehicle['name']}, Description: {vehicle['description']}, Price: {vehicle['price']}")
    else:
        print("Error:", response.status_code, response.json())

# Test the functions
if __name__ == '__main__':
    add_vehicle("SUV", "A spacious SUV for family trips", 4000000)
    add_vehicle("Sedan", "A comfortable sedan for city commutes", 1200000)
    get_vehicles()
