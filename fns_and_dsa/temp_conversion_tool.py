FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
def convert_to_celsius(fahrenheit):
    temprature_in_celsius = (fahrenheit-32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return temprature_in_celsius
def convert_to_fahrenheit(celsius):
    temprature_in_fahrenheit = (celsius*9/5) + 32
    return temprature_in_fahrenheit

def main():
      
    while True:
     try: 
        user_temp = float(input("Enter the temperature to convert:"))
        user_unit = input("Is this temperature in Celsius or Fahrenheit? (C/F):")

        if user_unit == "C":
           converted_temp = convert_to_fahrenheit(user_temp)
        elif user_unit == "F":
           converted_temp = convert_to_celsius(user_temp)
        else:
            print("Invalid temperature. Please enter a numeric value.")
        print(f"{user_temp:.1f}°{user_unit} is {converted_temp:.1f}°")
     except ValueError as e:
      print(f"Error: {e}")   

if __name__ == "__main__":
  main()