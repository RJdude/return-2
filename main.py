def Multiply(num1, num2):
  return num1 * num2


def shopping():
  jeansPrice = 40
  amountPairs = 6

  total = Multiply(jeansPrice, amountPairs)
  print("total price is", total)


def episodes():
  watched = 12
  time = 50
  total = Multiply(watched, time)
  print("episodes watched is", total)
shopping()
episodes()

