# Inventory System

This project consists of creating a simple inventory system for a store, with the objective of automating the process of registering products and storing the information in a CSV file. Furthermore, it is useful for calculating statistics such as the most expensive product and the highest inventory.

## Project Structure

The project is organized into the following files:

- **app.py**  
  Entry point of the application. It initializes and runs the system.

- **menu.py**  
  Defines the menu structure using a dictionary to manage user options.

- **option.py**  
  Handles the logic associated with each menu option, acting as a bridge between the user interface and core processes.

- **processes.py**  
  Contains the core functionalities of the system, including product registration, display, statistics calculation, search, deletion, and updates.

- **validations.py**  
  Provides input validation utilities to ensure data integrity, such as numeric checks and non-empty inputs.

- **csv_manager.py**  
  Manages data persistence by handling reading from and writing to CSV files.

## Sample Data

| Product | Price per Unit | Amount |
|--------|------|----------|
| Apple  | 2000 | 10       |
| Milk   | 3000 | 5        |


## FlowChart
![Flowchart](Images/Inventory.png)

## Author

Daniel Mendoza  
Systems Engineer | Aspiring Software Developer
