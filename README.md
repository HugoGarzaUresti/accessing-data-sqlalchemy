# Accessing Data with SQLAlchemy

This project demonstrates how to create a Flask application that uses SQLAlchemy to store and retrieve data in a relational database.

## Requirements

- Python 3.x
- Flask
- Flask-SQLAlchemy

## Setup

1. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

2. Run the application:
    ```sh
    python run.py
    ```

3. Open your browser and navigate to:
    - List Customers: `http://127.0.0.1:5000/customers`
    - Add Customer: `http://127.0.0.1:5000/add-customer`

## Code Explanation

### `app/__init__.py`

This file initializes the Flask application and sets up SQLAlchemy.

### `app/models.py`

This file defines the `Customer` model, which represents the data structure.

### `app/routes.py`

This file contains the route handlers for displaying and adding customers.

### `templates/customers.html`

This template renders a list of customers.

### `templates/add_customer.html`

This template renders a form to add a new customer.

### `run.py`

This script serves as the entry point for the application and creates the database tables.
