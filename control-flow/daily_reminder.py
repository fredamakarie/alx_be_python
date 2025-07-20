task = input("Enter your task:")
priority = input("Please state the level of Priority (high/medium/low)")
time_bound = input("Is it time-bound? (Yes/No)")
match priority:
    case "high":
        if priority == "high" and time_bound == "Yes":
            print(task, "is a high priority task that requires immediate attention today!")
        else:
            print(task, "is a high priority task. Complete it as soon as possible.")

    case "medium":
        if priority == "medium" and time_bound == "Yes":
            print(task, "is a mid priority task that requires immediate attention today!")
        else:
            print(task, "is a mid priority task. Complete it as soon as possible.")

    case "low":
        if priority == "low" and time_bound == "Yes":
            print(task, "is a low priority task that requires immediate attention today!")
        else:
            print(task, "is a low priority task. Complete it when you have some free time.")




