def perform_operation(num1, num2, operation):
    match operation:
        case "add":
            num1 + num2
        case "subtract":
            num1 - num2
        case "multiply":
            num1 * num2
        case "divide":
            num1 / num2
        case _:
            print("Cannot divide by zero")

