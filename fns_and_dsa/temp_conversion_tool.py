FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    C = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

convert_to_celsius()

def convert_to_fahrenheit(celsius):
    F = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
convert_to_fahrenheit()

temperature = float(input("Enter the temperature to convert: "))
unit = "Is this temperature in Celsius or Fahrenheit? (C/F): "
if unit == "C":
    celsius = temperature
    print(f"{celsius}°C is {convert_to_celsius(celsius)}")
if unit == "F":
    fahrenheit = temperature
    print(f"{fahrenheit}°F is {convert_to_celsius(fahrenheit)}°C")
else:
    print("Please try again")