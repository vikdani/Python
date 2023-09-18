'''The Lifetime Supply Calculator

Write a function named calculateSupply that:
takes 2 arguments: age, amount per day.
calculates the amount consumed for rest of the life (based on a constant max age).
outputs the result to the screen like so: "You will need NN to last you until the ripe old age of X"
Call that function three times, passing in different values each time.'''


def  calculateSupply(age,amount_per_day):
    max_age = 80
    remaining_age = max_age - age
    amount_per_year = amount_per_day * 365
    total_supply = amount_per_year * remaining_age
    return total_supply


output1 = calculateSupply(20,3)
print(f"You will need {output1} to last you until the ripe old age of 80")
output2 = calculateSupply(30,4)
print(f"You will need {output2} to last you until the ripe old age of 80")
output3 = calculateSupply(45,5)
print(f"You will need {output3} to last you until the ripe old age of 80")
