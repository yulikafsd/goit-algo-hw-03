from hw_03_1 import get_days_from_today
from hw_03_2 import get_numbers_ticket
from hw_03_3 import sanitized_numbers
from data import raw_numbers, users
from hw_03_4 import get_upcoming_birthdays

print('\n')
print('Завдання 1:', '-'*40)
get_days_from_today()
print('\n')

print('Завдання 2:', '-'*40)
get_numbers_ticket()
print('\n')

print('Завдання 3:', '-'*40)
sanitized_numbers(raw_numbers)
print('\n')

print('Завдання 4:', '-'*40)
get_upcoming_birthdays(users)