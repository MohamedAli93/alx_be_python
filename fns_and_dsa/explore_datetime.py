from datetime import datetime

def display_current_datetime():
  current_date = datetime.datetime.now()
  formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
  print(f"Current date and time: {formatted_datetime}")

def calculate_future_date():
  number_of_days = int(input("Enter the number of days: "))
  delta = datetime.timedelta(days=number_of_days)
  day = datetime.datetime.now()
  future_date = day + delta
  formatted_future_date = future_date.strftime("%Y-%m-%d")
  print(f"The date {number_of_days} days from now will be: {formatted_future_date}")
display_current_datetime()
calculate_future_date()