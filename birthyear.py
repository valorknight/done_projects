# birth_year = input('what year were you born? ')
# age = (2021 - int(birth_year))
# print(f'Your age is {age}')

# To find using current year

from datetime import date

current_date = date.today()

current_year = current_date.year
# print(current_year)

# print(f'Current year is  {current_year}')

birth_year = input('what year were you born? ')

age = current_year - int(birth_year)
print(f'Your age is {age}')