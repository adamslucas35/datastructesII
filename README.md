# WGUPS Delivery System

This project is a delivery system for the Western Governors University Parcel Service (WGUPS). It provides an algorithm and implementation to route delivery trucks and ensure timely and efficient delivery of packages while meeting their specific requirements. The system is designed to keep the total distance traveled by the trucks under 140 miles.

## Scenario

The WGUPS has three trucks, two drivers, and an average of 40 packages to deliver each day in Salt Lake City. Each package has unique criteria and delivery requirements. The goal is to deliver all 40 packages on time, considering their specific constraints, and minimize the total distance traveled by the trucks.

## Features

- Routing algorithm: The system includes an algorithm to determine the most efficient route for each truck based on the package delivery requirements and distances between locations.
- Package management: Packages are loaded onto trucks according to special constraints and are tracked throughout the delivery process. The system keeps track of package status, departure times, and delivery times.
- Hash table: The project includes a hash table data structure for efficient retrieval of package information based on package IDs.
- Console interface: The system provides a console interface where the user can enter a specific time to check the status of all packages at that time.

## Dependencies

The project requires the following files and data:

- `main.py`: The main script that runs the delivery system.
- `truck.py`: Defines the Truck class used to represent delivery trucks.
- `package.py`: Defines the Package class used to represent individual packages.
- `hasher.py`: Implements the HashTable class for efficient package retrieval.
- `csvLoader.py`: Contains functions to load package information from CSV files.
- `C950_ALUC167_DOCS/WGUPS_Distances.csv`: CSV file containing distance data between locations.
- `C950_ALUC167_DOCS/WGUPS_Addresses.csv`: CSV file containing address data for locations.
- `C950_ALUC167_DOCS/WGUPS_Package.csv`: CSV file containing package data.

## Usage

1. Ensure you have Python installed on your system (version X.X.X or higher).
2. Clone this repository to your local machine.
3. Place the required CSV files (`WGUPS_Distances.csv`, `WGUPS_Addresses.csv`, and `WGUPS_Package.csv`) in the `C950_ALUC167_DOCS` directory.
4. Open a terminal or command prompt and navigate to the project directory.
5. Run the following command to start the delivery system:

   ```bash
   python main.py
   ```

6. Follow the prompts in the console interface to interact with the system.
7. Enter a time in HH:MM format to check the status of all packages at that time.

## Conclusion

The WGUPS Delivery System provides an efficient solution for routing delivery trucks and ensuring timely package delivery while considering various constraints. The project incorporates non-linear data structures, hashing algorithms, dictionaries, and sets to organize and manage package data effectively. The implementation follows self-adjusting data structure principles and aims to optimize the performance of the application.

The system can be easily extended to handle deliveries in other cities by providing the corresponding distance and address data in CSV format.

For more details on the implementation and design decisions, please refer to the source code and comments within the files.

---
