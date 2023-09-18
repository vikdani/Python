def find_clock_angle(hour,minute):
   roundoffhour = hour + (minute/60) * 1/3

   hour_angle = (roundoffhour%12) * 30 # hour consist of 30 degree
   minute_angle = (minute%60) * 6      # minute consist of 6 degree

   angle = abs(hour_angle - minute_angle)

   angle = min(angle,360-angle)


   return angle

def main():
   hour = int(input("enter value of hour (0-12) :"))
   minute = int(input("enter value of minute (0-59) :"))
   angle = find_clock_angle(hour,minute)
   print("the angle between hour and minute is",angle)


main()    
                