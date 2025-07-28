def perform_operation(num1, num2, operation):
    if operation == "add":
        num1 + num2
    elif operation == "subtract":
        num1 - num2
    elif operation == "add":
        num1 * num2
    elif operation == "add":
        num1 / num2
    elif num2 == 0:
        print("Cannot divide by zero")
    else:
        print("These values are not valid")
    # match operation:
    #     case "add":
    #         num1 + num2
    #     case "subtract":
    #         num1 - num2
    #     case "multiply":
    #         num1 * num2
    #     case "divide":
    #         num1 / num2
    #     case _:
    #         print("Cannot divide by zero")

