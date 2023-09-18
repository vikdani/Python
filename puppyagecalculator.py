'''The Puppy Age Calculator : Write a function named calculateDogAge that:
takes 1 argument: your puppy's age. calculates your dog's age based on the conversion rate of 1 
human year to 7 dog years. outputs the result to the screen like so: 
"Your doggie is NN years old in dog years! "Call the function three times with different sets of values.
Bonus: Add an additional argument to the function that takes the conversion rate of human to dog years.'''
def  calculateDogAge(puppy_age,human_year=7):
    puppy_age = puppy_age *  human_year 
  
    return puppy_age

o1 =(calculateDogAge(2))
print(f"Your doggie is {o1} years old in dog years! ")

o2=(calculateDogAge(4))
print(f"Your doggie is {o2} years old in dog years! ")

o3 =(calculateDogAge(6))
print(f"Your doggie is {o3} years old in dog years! ")
 
   