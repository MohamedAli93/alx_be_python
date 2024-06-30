task = input("Enter your task: ")
priority = str(input("Priority (high/medium/low): ")).lower()
time_bound = str(input("Is it time-bound? (yes/no): ")).lower()
reminder1 = f"Reminder: {task} is a {priority} priority task "
reminder2 = f"Note: {task} is a {priority} priority task "
if time_bound == "yes":
    reminder1 += "that requires immediate attention today!"
    reminder2 += "that requires immediate attention today!"
elif time_bound == "no":
    reminder1 += "Consider completing it when you have free time."
    reminder2 += "Consider completing it when you have free time."
match priority:
    case "high":
        print(reminder1)
    case "medium":
        print(reminder2)
    case "low":
        print(reminder2)
    case _:
        print("Invalid priority level. Reminder not created.")