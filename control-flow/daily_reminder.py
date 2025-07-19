task = input("Please add the task for the day")
priority = input("Please state the level of priority (High/Medium/Low)")
time_bound = input("Is it time bound? (Yes/No)")
match priority:
    case "High":
        if priority == "High" and time_bound == "Yes":
            print (task, "is a high priority task that requires immediate attention today!")
        else:
            print (task, "is a high priority task. Complete it as soon as possible.")

    case "Medium":
        if priority == "Medium" and time_bound == "Yes":
            print (task, "is a mid priority task that requires immediate attention today!")
        else:
            print (task, "is a mid priority task. Complete it as soon as possible.")

    case "Low":
        if priority == "Low" and time_bound == "Yes":
            print (task, "is a low priority task that requires immediate attention today!")
        else:
            print (task, "is a low priority task. Complete it when you have some free time.")




