numbers = int(input('How many numbers? '))

a = int(0)
b = int(1)

list_ = [a , b]

repeat_ = "yes"



# print(list_)
while numbers >= 1:
  num1 = list_[-1]
  num2 = list_[-2]
  o = num1 + num2

  list_.append(o)
  # y = x + b
  # z = y

  # list_.append(x)
  # list_.append(z)

  numbers -= 1



print(list_)