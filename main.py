def multiply(num1, num2):
  return (num1 * num2)

def hourToMins(num1):
  return num1/60

def shopping():
  jeansPrice = 40
  amountPairs = 6
  
  total = multiply(jeansPrice, amountPairs)
  print("total price is", total)
def episodes():
  watched = 12
  time = 50
  timeInMins = hourToMins(time)
  total = multiply(watched, time)
  print("episodes watched is", total)

shopping()
episodes()

