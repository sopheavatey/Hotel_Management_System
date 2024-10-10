

# Authentication
def requires_authentication(func):

   pass

def update_room_price(user, room, new_price):

   pass

def update_room_availability(user, room, available):

   pass


# testing the authentication
# Define a simple Room class
class Room:
    def __init__(self, number, price, available):
        pass

    def set_price(self, price):
        pass

    def set_availability(self, available):
        pass

# Create a sample room
room101 = Room(101, 100, True)

# Test the update_room_price and update_room_availability functions
update_room_price(manager, room101, 120)  # Should succeed
update_room_price(guest, room101, 120)    # Should fail (guest is not authenticated)
update_room_availability(manager, room101, False)  # Should succeed
update_room_availability(guest, room101, False)    # Should fail (guest is not authenticated)

 