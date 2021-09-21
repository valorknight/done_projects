import random
import time

no_of_rolls = int(input("How many dice? "))
min = 1
max = 6

# a = random.randint(min,max)
# b = random.randint(min,max)
# c = a + b

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
  print("Rolling the dices...")
  time.sleep(1)
  print("The values are...")
  time.sleep(1)

  a = random.randint(min,max)
  b = random.randint(min,max) 
  c = a + b

  if no_of_rolls == 1:
    print(a)
  elif no_of_rolls == 2:
    print(a)
    print(b)
    print(f'Sum of the values is {c}')
  else:
    print('wrong input')
    no_of_rolls = int(input("How many dices? "))
  roll_again = input("Roll again? ")
  # if roll_again == False:
  #   break