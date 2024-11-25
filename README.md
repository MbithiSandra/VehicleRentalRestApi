
# Vehicle Rental REST API
# MBITHI SANDRA MINOO 167253 BBIT C

This project is a simple Vehicle Rental REST API built with Flask. It allows users to manage vehicles by adding and retrieving them via HTTP requests. It also includes a client script to test the API functionality.

---

## Features
- Add a new vehicle
- Retrieve a list of all vehicles
- Simple and user-friendly API

---

## Requirements

Ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package installer)

---

## Setup Instructions

1. **Clone the repository**
   - Clone the repository or copy the files into a local directory on your computer.

2. **Set up the environment**
   - Open a terminal and navigate to the directory where the files are located.
   - Install the required dependencies using:
     ```bash
     pip install flask requests
     ```

3. **Run the API server**
   - Run the `app.py` file to start the Flask server:
     ```bash
     python app.py
     ```
   - You should see a message indicating the server is running:
     ```
     * Running on http://127.0.0.1:5000/
     ```
   - Open a browser or tool like Postman and visit `http://127.0.0.1:5000/` to see the welcome message.

4. **Testing the API**
   - To test the API endpoints:
     - Add `/vehicles` to the URL for all operations.
     - For example, to get a list of all vehicles, make a `GET` request to:
       ```
       http://127.0.0.1:5000/vehicles
       ```

---

## Running the Client Script

1. **Usage**
   - To interact with the API programmatically, run the client script section at the end of `app.py`. 
   - It includes functions to:
     - Add vehicles
     - Retrieve the list of vehicles

2. **Run the Client**
   - After starting the server, use the same terminal or open another terminal and run:
     ```bash
     python app.py
     ```

---

## API Endpoints

### **POST /vehicles**
Add a new vehicle to the list.

- **Request body:**
  ```json
  {
    "name": "Vehicle Name",
    "description": "Vehicle Description",
    "price": Vehicle Price
  }

  
If you intend to run the server (app.py), use the following command:

python app.py

Ensure you're in the correct directory where app.py is located before executing the command.

To use the client portion in the script, ensure the Flask server is running on http://127.0.0.1:5000/ before invoking any functions in the script.