def safe_divide(numerator, denominator):
    try:
        if denominator == 0:
            raise ZeroDivisionError ("Error: Cannot divide by zero.")
        else:
            float(numerator)
            float(denominator)
            return  f"The result of the division is{numerator/denominator}"
    except ValueError:
        return "Error: Please enter numeric values only."
   