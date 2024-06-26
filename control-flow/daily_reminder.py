task = input("Enter your task: ")
priority = str(input("Priority (high/medium/low): ")).lower()
time_bound = str(input("Is it time-bound? (yes/no): ")).lower()
match priority:
    case "high":
        reminder = f"{task} is a {priority} priority task "
    case "medium":
        reminder = f"{task} is a {priority} priority task "
    case "low":
        reminder = f"{task} is a {priority} priority task "
    case _:
        print("Invalid priority level. Reminder not created.")
if time_bound == "yes":
    reminder += "that requires immediate attention today!"
elif time_bound == "no":
    reminder += "Consider completing it when you have free time."
print("Reminder:", reminder)