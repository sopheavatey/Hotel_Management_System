# Authentication decorator (no *args, **kwargs)
def requires_authentication(func):
    def wrapper(user, room, value):
        if user['is_authenticated']:  # Check if the user is authenticated
            return func(user, room, value)  # Call the function if authenticated
        else:
            print("Access denied. User is not authenticated.")  # Deny access
    return wrapper

# Price Descriptor
class PriceDescriptor:
    def __get__(self, instance, owner):
        return instance._price

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        instance._price = value

# Availability Descriptor
class AvailabilityDescriptor:
    def __get__(self, instance, owner):
        return instance._available

    def __set__(self, instance, value):
        if not isinstance(value, bool):
            raise ValueError("Availability must be a boolean value")
        instance._available = value

# Room class with descriptors
class Room:
    price = PriceDescriptor()  # Uses PriceDescriptor
    available = AvailabilityDescriptor()  # Uses AvailabilityDescriptor

    def __init__(self, number, price, available):
        self.number = number
        self._price = price  # Assigns to PriceDescriptor
        self._available = available  # Assigns to AvailabilityDescriptor

    def set_price(self, price):
        self.price = price  # Uses descriptor

    def set_availability(self, available):
        self.available = available  # Uses descriptor

# Predefined rooms for the hotel
predefined_rooms = {
    101: Room(101, 100, True),
    102: Room(102, 120, False),
    201: Room(201, 200, True),
    202: Room(202, 220, True)
}

# Functions to update room properties (with authentication)
@requires_authentication
def update_room_price(user, room, new_price):
    room.set_price(new_price)

@requires_authentication
def update_room_availability(user, room, available):
    room.set_availability(available)

# Function to view all rooms
def view_all_rooms():
    print ("\n===================================")
    print("Hotel Room Overview:")
    for number, room in predefined_rooms.items():
        availability = "Available" if room.available else "Unavailable"
        print(f"Room {number}: ${room.price}, {availability}")
    print ("===================================")

# Function to view available rooms (guest view)
def view_available_rooms():
    print ("\n===============================")
    print("Available Rooms:")
    for number, room in predefined_rooms.items():
        if room.available:
            print(f"Room {number}: ${room.price}")
    print ("===============================")

# Manager options (protected by password)
def manager_menu():
    username = "manager123"
    password = "admin123"  # Predefined password for manager
    
    entered_username = input("\nEnter username: ")
    if entered_username != username:
        print("Incorrect username! Access denied.")  
        return 
    
    entered_password = input("Enter password: ")
    
    if entered_password == password:
        print("\nLogin successful! Welcome, manager.")
        
        while True:
            print ("\n \n")
            print("---------OPTIONS---------")
            print("1. Update Room Price")
            print("2. Update Room Availability")
            print("3. View All Room Details")
            print("4. Logout")
            choice = input("\nSelect an option (1/2/3/4): ")

            if choice == "1":
                try:
                    room_number = int(input("\nEnter room number: "))
                    if room_number in predefined_rooms:
                        new_price = float(input("Enter new price: "))
                        update_room_price({"is_authenticated": True}, predefined_rooms[room_number], new_price)
                        print(f"\nSuccessfully updated the price for room {room_number} to ${predefined_rooms[room_number].price}")
                    else:
                        print("Invalid room number.")
                except ValueError as e:
                    print(f"Error: {e}")
            elif choice == "2":
                try:
                    room_number = int(input("\nEnter room number: "))
                    if room_number in predefined_rooms:
                        new_availability = input("\nEnter new availability (True/False): ").lower() == "true"
                        update_room_availability({"is_authenticated": True}, predefined_rooms[room_number], new_availability)
                        availability = "Available" if predefined_rooms[room_number].available else "Unavailable"
                        print(f"\nSuccessfully updated the status for room {room_number} to {availability}")
                    else:
                        print("Invalid room number.")
                except ValueError as e:
                    print(f"Error: {e}")
            elif choice == "3":
                view_all_rooms()
            elif choice == "4":
                print("\nLogging out...")
                break
            else:
                print("Invalid choice, please try again.")

    else:
        print("Incorrect password. Access denied.")
    


# Guest options (no authentication required)
def guest_menu():
    print("\nWelcome, guest! Here are some of the available rooms in our hotel")
    view_available_rooms()

# Main function
def main():
    print("\n")
    print("                             *~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*")
    print("                              Welcome to the Hotel Management System")
    print("                             *~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*")
    while True:
        print("\n")
        print("------OPTIONS------")
        print("1. Manager Login")
        print("2. Guest View")
        print("3. Exit")
        role = input("\nSelect an option (1/2/3): ")

        if role == "1":
            manager_menu()
        elif role == "2":
            guest_menu()
        elif role == "3":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
