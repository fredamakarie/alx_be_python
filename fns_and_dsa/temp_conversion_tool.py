FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5)


def convert_to_celsius(fahrenheit) ():
    C = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

convert_to_celsius(fahrenheit) ()

def convert_to_fahrenheit(celsius) ():
    F = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
convert_to_fahrenheit(celsius) ()

temperature = input("Enter the temperature to convert: ")
"Is this temperature in Celsius or Fahrenheit? (C/F): "