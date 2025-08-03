def safe_divide(numerator, denominator):
    try:
        if denominator == 0:
            raise ZeroDivisionError ("Cannot divide by zero")
        else:
            return  f"The result of the division is{numerator/denominator}"
    except ValueError:
        return "Please enter numeric values only"
    