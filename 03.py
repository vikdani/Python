
class ReservationSystem:
        def __init__(self, num_seats): # initialize the list containing seats
            self.LIST = [0] * num_seats # num_seats are all elements inside list and are initialize to zero

        def set_capacity(self, num_seats):
            self.LIST = [0] * num_seats
            print("Seating capacity set to {}.".format(num_seats)) # assign seating capacity equal to num_seats entered by user

        def assign_seat(self, seat_number):
            if 1 <= seat_number and seat_number<= len(self.LIST):  # check for seat number if it is positive and is in range of list provided
                if self.LIST[seat_number - 1] == 0: # check whether seat is occupied or not, 0 means unoccupied
                    self.LIST[seat_number - 1] = 1 # if not occupied ,assign seat and set 1 to it
                    print("Seat " + str(seat_number) + " assigned successfully.")
                    return True  # Seat assigned successfully
                else:
                    print("Seat " + str(seat_number) + " is already occupied.")

                    return False  # Seat already occupied
            else:
                print("Invalid seat number.")
                return False  # Invalid seat number

        def get_seating_chart(self):
            return self.LIST

        def is_all_seats_filled(self):
            return all(LIST == 1 for LIST in self.LIST)


def main():
        capacity = int(input("Enter the capacity of seating: "))
        reservation_system = ReservationSystem(capacity)

        # Assign seats until all seats are filled
        while not reservation_system.is_all_seats_filled(): # calling function for assigning the seats
            seat_number = int(input("Enter the seat number to assign: "))
            reservation_system.assign_seat(seat_number) # this particular block is used for assigning the seat till the seating capacity is not full

        # Get seating chart
        seating_chart = reservation_system.get_seating_chart()
        print("Seating Chart:", seating_chart)
    
main()
