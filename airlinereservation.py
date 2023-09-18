class AirlineReservationSystem:
    def __init__(self):
        self.LIST = [0] * 10

    def assign_seat(self, choice, number_seat):
        if choice == 1:
            if number_seat >= 1 and number_seat <= 5:
                if self.LIST[number_seat - 1] == 0:
                    self.LIST[number_seat - 1] = 1
                    print("Seat " + str(number_seat) + " is successfully assigned.")
                    print("Your seat is in the smoking zone, and the seat number is", str(number_seat))
                else:
                    print("Seat " + str(number_seat) + " is already occupied.")
            else:
                print("Invalid seat.")
        elif choice == 2:
            if number_seat >= 6 and number_seat <= 10:
                if self.LIST[number_seat - 1] == 0:
                    self.LIST[number_seat - 1] = 1
                    print("Seat " + str(number_seat) + " is successfully assigned.")
                    print("Your seat is in the non-smoking zone, and the seat number is", str(number_seat))
                else:
                    print("Seat " + str(number_seat) + " is already occupied.")
            else:
                print("Invalid seat.")
        else:
            print("Wrong selection. Select again.")
            
    def get_seating_chart(self):
            return self.LIST         

   # def boarding_pass(self, choice, number_seat):
       # if choice == 1:
          #  print("Your seat is in the smoking zone, and the seat number is", str(number_seat))
       # elif choice == 2:
            #print("Your seat is in the non-smoking zone, and the seat number is", str(number_seat))
       # else:
        #    print("Wrong choice.")

    def is_all_seats_filled_for_smoking(self):
        return all(LIST == 1 for LIST in self.LIST[0:5])

    def is_all_seats_filled_for_non_smoking(self):
        return all(LIST == 1 for LIST in self.LIST[5:10])


def main():
    Airline_reservation = AirlineReservationSystem()

    while not Airline_reservation.is_all_seats_filled_for_smoking() or not Airline_reservation.is_all_seats_filled_for_non_smoking():
        choice = int(input("Enter your choice: Select 1 for the smoking section and Select 2 for the non-smoking section: "))
        number_seat = int(input("Enter the seat number to assign: "))
    
        if choice == 1 or choice == 2:
            if choice == 1 and Airline_reservation.is_all_seats_filled_for_smoking():
                print("Smoking section is full.")
                answer = input("Do you accept to be placed in the non-smoking section? (yes/no): ") 
                if answer.lower() == "yes":
                    choice = 2
                else:
                    print("Next flight leaves in 3 hours.")
                    break
            elif choice == 2 and Airline_reservation.is_all_seats_filled_for_non_smoking():
                print("Non-smoking section is full.")
                answer = input("Do you accept to be placed in the smoking section? (yes/no): ")
                if answer.lower() == "yes":
                    choice = 1
                else:
                    print("Next flight leaves in 3 hours.")
                    break
            else:

                Airline_reservation.assign_seat(choice, number_seat)

                if  Airline_reservation.is_all_seats_filled_for_smoking() and  Airline_reservation.is_all_seats_filled_for_non_smoking():
                    print("All seats are full") 
        else:
            print("Invalid choice. Please select again.")

  #  Airline_reservation.boarding_pass(choice, number_seat)
    seating_chart = Airline_reservation.get_seating_chart()  
    print("seating chart is :",seating_chart)

main()

