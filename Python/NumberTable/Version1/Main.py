
import sys

def checkSymbol(symbol):
  acceptedSymbol = ['+', '-', '*', '/']
  if not symbol in acceptedSymbol:
    print("That is not a symbol")
    sys.exit()

def checkNum(num):
  try:
    num = int(num)
  except:
    print("That is not a number")
    sys.exit()

symbol = input("What operation do you wish to complete?: ")
checkSymbol(symbol)
number = input("What number would you like it to be completed on?: ")
checkNum(number)
number = int(number)

ops = {"+": (lambda x,y: x+y), 
       "-": (lambda x,y: x-y), 
       "/": (lambda x,y: round(x/y, 2)),
       "*": (lambda x,y: x*y)}

nums = range(0, number + 1)

toPrint = "{} |".format(symbol)
for num in nums:
  toPrint = "{} {}".format(toPrint, num)

print("{}\n".format(toPrint))

for num in nums:
  toPrint = "{} |".format(num)

  for x in range(number + 1):
    try:
      toPrint = "{} {}".format(toPrint, ops[symbol](num, x))
    except ZeroDivisionError:
      toPrint = "{} Na".format(toPrint)

  print(toPrint)
