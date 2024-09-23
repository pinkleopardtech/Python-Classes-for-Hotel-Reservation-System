Hotel Reservation System
Project Overview
This is a Python-based Hotel Reservation System designed to manage hotel bookings, guest details, room availability, and payment processing. It employs Object-Oriented Programming (OOP) principles and consists of four main classes: Room, Guest, Reservation, and Payment. The system can calculate total booking prices based on room type and stay duration and process payments using various payment methods.

Key Features:
Room availability check.
Guest information management.
Reservation creation and modification.
Automatic total price calculation based on the number of nights.
Payment processing simulation.
Project Structure
The project consists of the following main components:

Room Class: Handles room details such as room number, type, price per night, and availability.
Guest Class: Manages guest information including name, email, and phone number.
Reservation Class: Manages hotel reservations by associating guests with rooms and calculating the total price.
Payment Class: Processes the payments for reservations.
Installation
To use this project, ensure you have the following software and dependencies installed on your local machine:

Python 3.x: This project is built in Python and requires a Python 3.x interpreter.
Steps to run:
Clone the repository from GitHub:

bash
Copy code
git clone https://github.com/pinkleopardtech/hotel-reservation-system.git
Navigate to the project directory:

bash
Copy code
cd hotel-reservation-system
Run the Python script to simulate hotel reservations:

bash
Copy code
python hotel_reservation_system.py
Usage Instructions
Creating a Room Object
python
Copy code
room1 = Room(101, "Double", 100.00, "Available")
This code creates a room object with the room number 101, room type Double, price per night as 100.00, and sets the room's status to Available.

Creating a Guest Object
python
Copy code
guest1 = Guest("Ted Vera", "tedvera@example.com", "555-1234")
This code creates a guest object with the name "Ted Vera", email "tedvera@example.com", and phone number "555-1234".

Creating a Reservation
python
Copy code
from datetime import datetime
check_in = datetime(2024, 9, 23)
check_out = datetime(2024, 9, 25)
reservation1 = Reservation(1, guest1, room1, check_in, check_out)
This code creates a reservation object for a stay from September 23, 2024, to September 25, 2024 for guest Ted Vera.

Calculating Total Price
python
Copy code
total_price = reservation1.calculate_total_price()
print(f"Total Price: ${total_price}")
The calculate_total_price() method calculates the total cost of the stay based on the room's price per night and the number of nights.

Processing Payment
python
Copy code
payment1 = Payment(1, "Credit Card", total_price)
payment1.process_payment()
This code processes a payment of the total price using the "Credit Card" payment method.

Contributing
Contributions are welcome! Here’s how you can contribute to the project:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Commit your changes (git commit -m "Add some feature").
Push to the branch (git push origin feature-branch).
Open a pull request.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
For any questions or issues, feel free to open an issue on this repository or contact me at networkjocker@gmailcom.

Acknowledgments
Special thanks to everyone who contributed to this project and helped refine the system through feedback and suggestions.

