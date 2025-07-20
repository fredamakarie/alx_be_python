task = input("Enter your task:")
time_bound = input("Is it time-bound? (Yes/No)")
priority = input("Priority (high/medium/low)")

match priority:
    case "high":
        if priority == "high" and time_bound == "Yes":
            print("Reminder:", task, "is a high priority task that requires immediate attention today!")
        else:
            print("Reminder:", task, "is a high priority task. Complete it as soon as possible.")

    case "medium":
        if priority == "medium" and time_bound == "Yes":
            print("Reminder:", task, "is a mid priority task that requires immediate attention today!")
        else:
            print("Reminder:", task, "is a mid priority task. Complete it as soon as possible.")

    case "low":
        if priority == "low" and time_bound == "Yes":
            print("Reminder:", task, "is a low priority task that requires immediate attention today!")
        else:
            print("Note:", task, "is a low priority task. Complete it when you have some free time.")




