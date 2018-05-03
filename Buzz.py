number = int(input("Enter number"))
def fizzbuzz():
    if number % 15 == 0:
      print("fizzbuzz:")
    elif number % 3 == 0:
      print("fizz")
      
    elif number % 5 == 0:
      print("buzz")
    else:
      print("this is not fizz buzz")
fizzbuzz() 