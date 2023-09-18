''' Write a program to calculate the angle between the hands of a clock
This is pretty self explanatory just take into account that the hour hand moves in
increments, such that at 20 minutes past it has moved 1/3 of an hour.'''

def calculate_clock_angle(hour, minute):
   
    hour_angle = 0.5 * (hour * 60 + minute)
    minute_angle = 6 * minute

    # Calculate the absolute difference between the two angles                                                                  
    angle = abs(hour_angle - minute_angle)

    # Take the smaller angle between the two possible angles (clockwise or counterclockwise)
    angle = min(angle, 360 - angle)

    return angle

def main():
    hour = int(input("Enter the hour (0-12): "))
    minute = int(input("Enter the minute (0-59): "))

    angle = calculate_clock_angle(hour, minute)
    print(f"The angle between the clock hands is {angle} degrees.")
main()

    