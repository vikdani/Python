'''The Temperature Converter

Create a function called celsiusToFahrenheit:

Store a celsius temperature into a variable.
Convert it to fahrenheit and output "NN°C is NN°F".

Create a function called fahrenheitToCelsius:

Now store a fahrenheit temperature into a variable.
Convert it to celsius and output "NN°F is NN°C."'''

def celsiusToFahrenheit(celsius):
    celsius_temp = celsius
    temp_in_fahrenheit  = (celsius_temp * 9/5) + 32
    return temp_in_fahrenheit

def fahrenheitToCelsius(fahrenheit):
    fahrenheit_temp = fahrenheit
    temp_in_celsius = (fahrenheit_temp-32) *5/9
    return temp_in_celsius

def main():
    celsius = int(input("Enter temprature in celcius"))
    fahrenheit = int(input("Enter temprature in fahrenheit"))
    result1 = celsiusToFahrenheit(celsius)
    print(f"{celsius}°C is {result1}°F")
    result2 = celsiusToFahrenheit(fahrenheit)
    print(f"{fahrenheit}°F is {result2}°C")
main()    
