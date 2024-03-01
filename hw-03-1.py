# Розрахунок кількості днів між заданою і поточною датою 

from datetime import datetime
import re

def get_days_from_today():
    # Ввід дати користувачем:
    user_input = input('Введіть дату у форматі "дд.мм.рррр": ')
    
    # Оголошення довжини та формату вводу даних
    right_length = len(user_input) == 10
    date_pattern = r'\d{2}\.\d{2}\.\d{4}'
    right_format = re.search(date_pattern, user_input)
    
    # Перевірка довжини та формату вводу 
    if right_length and right_format:

        # Розрахування кількості днів
        try:
            user_date = datetime.strptime(user_input, "%d.%m.%Y")
            current_date = datetime.now()
            days_from_user_date = current_date.date() - user_date.date()

            # Обробка дати в минулому
            if days_from_user_date.days >= 0:
                print(f'Від заданої дати пройшло {days_from_user_date.days} днів')
            # Обробка дати в майбутньому
            else:
                print(f'До заданої дати залишилось {-(days_from_user_date.days)} днів')
        
        # Обробка введення неіснуючої дати з рекурсією
        except ValueError:
            print('Такої дати не існує. Спробуйте ввести іншу дату.')
            get_days_from_today()
    
    # Обробка введення дати в невірному форматі з рекурсією
    else:
        print('Дата введена у невірному форматі.\nСпробуйте знову у форматі "дд.мм.рррр".')
        get_days_from_today()

get_days_from_today()