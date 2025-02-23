# Importing necessary libraries
from flask import Flask, request, jsonify  # Flask for building the web app, request to handle API inputs, jsonify for formatting outputs
import re  # Regular expressions module for email validation
import requests  # To make external API calls to fetch profile pictures

# Step 1: Define the Employee class to represent an employee using Object-Oriented Programming (OOP)
class Employee:
    def __init__(self, name, age, email, position):
        # Initializing the employee's attributes
        self.name = name  # Employee name
        self.age = age  # Employee age
        self.email = email  # Employee email
        self.position = position  # Employee position (e.g., 'Developer', 'Manager')

    # Method to update employee information
    def update_info(self, name=None, age=None, email=None, position=None):
        # Update only provided attributes
        if name:  # If name is provided, update it
            self.name = name
        if age:  # If age is provided, update it
            self.age = age
        if email:  # If email is provided, update it
            self.email = email
        if position:  # If position is provided, update it
            self.position = position
        return self  # Return the updated employee object

# Step 2: Define the EmployeeManager class to manage the list of employees
class EmployeeManager:
    def __init__(self):
        self.employees = {}  # Dictionary to store employees, with employee ID as the key

    # Method to add an employee to the dictionary
    def add_employee(self, emp_id, employee):
        self.employees[emp_id] = employee  # emp_id is the key, employee object is the value

    # Method to list all employees (optional, but useful for managing employees)
    def list_employees(self):
        return self.employees  # Return the dictionary of all employees

# Step 3: Create a Flask app instance
app = Flask(__name__)  # 'app' is the Flask application object

# Step 4: Create an instance of EmployeeManager to manage employees
manager = EmployeeManager()  # This will hold and manage all employees

# Step 5: Define the /add_employee API endpoint to add new employees
@app.route('/add_employee', methods=['POST'])
def add_employee():
    data = request.get_json()  # Get the JSON data from the incoming POST request
    emp_id = data['id']  # Extract the employee ID from the request
    # Create an Employee object using the data
    employee = Employee(data['name'], data['age'], data['email'], data['position'])
    manager.add_employee(emp_id, employee)  # Add the employee to the manager
    return jsonify({"message": "Employee added successfully!"})  # Respond with a success message

# Step 6: Define the /list_employees API endpoint to list all employees
@app.route('/list_employees', methods=['GET'])
def list_employees():
    employees = {emp_id: vars(emp) for emp_id, emp in manager.employees.items()}  # Convert employee objects to dictionaries for JSON output
    return jsonify(employees)  # Respond with the list of employees in JSON format

# Step 7: Define a utility function to validate email addresses using regex
def validate_email(email):
    pattern = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'  # Simple regex pattern for validating an email
    return re.match(pattern, email) is not None  # Returns True if the email matches the pattern, else False

# Step 8: Define the /search_employee API endpoint to search employees by name
@app.route('/search_employee', methods=['GET'])
def search_employee():
    query = request.args.get('query')  # Get the 'query' parameter from the request's URL
    result = {emp_id: vars(emp) for emp_id, emp in manager.employees.items() if query.lower() in emp.name.lower()}  # Find employees whose name contains the query
    return jsonify(result)  # Respond with the search results in JSON format

# Step 9: Define a function that uses the request library to fetch an employee's profile picture from an external API
def fetch_profile_picture(email):
    response = requests.get(f'https://randomuser.me/api/?email={email}')  # Make a GET request to an external API
    if response.status_code == 200:  # Check if the request was successful
        return response.json()['results'][0]['picture']['thumbnail']  # Return the profile picture URL from the response
    return None  # If the request failed, return None

# Step 10: Run the Flask application when the script is executed
if __name__ == '__main__':
    app.run(debug=True)  # Start the Flask server with debug mode on
