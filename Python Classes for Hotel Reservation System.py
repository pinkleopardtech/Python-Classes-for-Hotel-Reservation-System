# Class for Room
class Room:
    def __init__(self, room_number, room_type, price_per_night, status):
        self.__room_number = room_number
        self.__room_type = room_type
        self.__price_per_night = price_per_night
        self.__status = status

    # Getter and Setter methods
    def get_room_number(self):
        return self.__room_number
    
    def set_room_number(self, room_number):
        self.__room_number = room_number

    def get_room_type(self):
        return self.__room_type

    def set_room_type(self, room_type):
        self.__room_type = room_type

    def get_price_per_night(self):
        return self.__price_per_night

    def set_price_per_night(self, price_per_night):
        self.__price_per_night = price_per_night

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

    # Method to check availability
    def check_availability(self):
        return self.__status == "Available"

# Class for Guest
class Guest:
    def __init__(self, guest_name, email, phone):
        self.__guest_name = guest_name
        self.__email = email
        self.__phone = phone

    # Getter and Setter methods
    def get_guest_name(self):
        return self.__guest_name
    
    def set_guest_name(self, guest_name):
        self.__guest_name = guest_name
    
    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_phone(self):
        return self.__phone
    
    def set_phone(self, phone):
        self.__phone = phone

# Class for Reservation
class Reservation:
    def __init__(self, reservation_id, guest, room, check_in_date, check_out_date):
        self.__reservation_id = reservation_id
        self.__guest = guest
        self.__room = room
        self.__check_in_date = check_in_date
        self.__check_out_date = check_out_date
        self.__total_price = 0

    # Getter and Setter methods
    def get_reservation_id(self):
        return self.__reservation_id
    
    def set_reservation_id(self, reservation_id):
        self.__reservation_id = reservation_id

    def get_guest(self):
        return self.__guest

    def set_guest(self, guest):
        self.__guest = guest

    def get_room(self):
        return self.__room

    def set_room(self, room):
        self.__room = room

    def get_check_in_date(self):
        return self.__check_in_date

    def set_check_in_date(self, check_in_date):
        self.__check_in_date = check_in_date

    def get_check_out_date(self):
        return self.__check_out_date

    def set_check_out_date(self, check_out_date):
        self.__check_out_date = check_out_date

    def get_total_price(self):
        return self.__total_price

    # Method to calculate total price based on room price and number of nights
    def calculate_total_price(self):
        num_nights = (self.__check_out_date - self.__check_in_date).days
        self.__total_price = num_nights * self.__room.get_price_per_night()
        return self.__total_price

# Class for Payment
class Payment:
    def __init__(self, payment_id, payment_method, amount):
        self.__payment_id = payment_id
        self.__payment_method = payment_method
        self.__amount = amount

    # Getter and Setter methods
    def get_payment_id(self):
        return self.__payment_id
    
    def set_payment_id(self, payment_id):
        self.__payment_id = payment_id

    def get_payment_method(self):
        return self.__payment_method

    def set_payment_method(self, payment_method):
        self.__payment_method = payment_method

    def get_amount(self):
        return self.__amount

    def set_amount(self, amount):
        self.__amount = amount

    # Method to process payment
    def process_payment(self):
        # Logic to process payment (e.g., credit card, PayPal)
        print(f"Processing {self.__payment_method} payment for amount: ${self.__amount}")

# Example of using the classes
from datetime import datetime

# Create room object
room1 = Room(101, "Double", 100.00, "Available")

# Create guest object
guest1 = Guest("Ted Vera", "tedvera@example.com", "555-1234")

# Create reservation object
check_in = datetime(2024, 9, 23)
check_out = datetime(2024, 9, 25)
reservation1 = Reservation(1, guest1, room1, check_in, check_out)

# Calculate total price
total_price = reservation1.calculate_total_price()
print(f"Total Price: ${total_price}")

# Create payment object and process payment
payment1 = Payment(1, "Credit Card", total_price)
payment1.process_payment()
