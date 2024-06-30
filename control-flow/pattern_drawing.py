square_length = int(input("Enter the size of the pattern:"))
while square_length <= 0:
    print("Please enter a positive integer.")
    square_length = int(input("Enter the size of the pattern:"))
row = 0
while row < square_length:
  col = 0
  while col < square_length:
    print("*", end="")
    col += 1
  print()
  row += 1