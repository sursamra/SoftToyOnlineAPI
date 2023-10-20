# Toy Store API Project

Welcome to the Soft Toy Online API, This api provides basic toy store operations built using Python and Flask!

## Description

This API  allows developers to browse, add, update, and remove toy products from an inventory. It's designed to help toy store owners manage their product catalog.

## Features

- **Browse Toys:** To view a list of available toys with details such as name, description, price, and quantity.

- **Add New Toys:** To add new toy products to the inventory, providing details like name, description, price, and quantity.

- **Update Toy Information:** This provides edit and update existing toy details, including name, description, price, and quantity.

- **Delete Toys:** To remove toys from the inventory.

- **Search and Filter:** To search for specific toys by name and filter by various criteria.

## Technologies Used

- Python
- Flask
- SQLAlchemy
- SQLite (to mimic a database)



## Setup

1. Create a directory Production_API
2. Switch to Production_API directory and Clone this repository.
3. Create a venv using `python -m venv softtoy`
4. Activate softtoy env using `softtoy\scripts\activate`
5. Install the required dependencies by running `pip install -r SoftToyOnlineAPI\requirements.txt`
6. Final directory structure should look like following

    - Production_API
      - SoftToyOnlineAPI
        - instance 
        - tests      
        - README.md


## Run Tests

Switch to Production_API directory and run tests using  `SoftToyOnlineAPI\tests\run_tests.bat`


## Run API

Switch to Production_API directory and run tests using  `SoftToyOnlineAPI\run_flask.bat`
API should be available at http://127.0.0.1:5000

Use Postman to api once in production mode

## Further Development

Pycharm is used to develop this api. SoftToyAPI directory can be opened to pycharm for further development.  

To develop further uncomment  this line app.py `#app.config['ENV'] = 'development'`. 


