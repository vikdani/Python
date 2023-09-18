'''The Geometrizer
Create 2 functions that calculate properties of a circle, using the definitions here.

Create a function called calcCircumfrence:

Pass the radius to the function.
Calculate the circumference based on the radius, and output "The circumference is NN".
Create a function called calcArea:

Pass the radius to the function.
Calculate the area based on the radius, and output "The area is NN".'''

def calcCircumfrence(radius):
    circumference = 2 * 3.14 *radius

    return circumference

def calcArea(radius):
    area_of_circle = 3.14 * radius *  radius
    return area_of_circle


result1 = calcCircumfrence(8)
print(f"The circumference is {result1}")

result2 = calcArea(9)
print(f"The area is {result2}")

