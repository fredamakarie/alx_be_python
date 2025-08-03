def safe_divide(numerator, denominator):
    try:
        result = float(numerator)/float(denominator)
        return  f"The result of the division is {result}"
    
    except ValueError:
        return "Error: Please enter numeric values only."
   
    finally: 
        denominator == 0
        raise ZeroDivisionError ("Error: Cannot divide by zero.")