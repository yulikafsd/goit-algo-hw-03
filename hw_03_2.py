import random

def get_range() -> tuple:

    print('Згенеруємо числа для лотереї!\n')
    
    while True:

    # Обробка винятку
        try:
            print('''Вам потрібно вввести мінімальні та максимальні числа, '''
                '''в проміжку між якими будуть згенеровані числа.''')
            
            # Отримуємо мінімальне значення
            min = 0
            while min < 1 or min > 1000:
                min = int(input('Введіть МІНімальне число в діапазоні від 1 до 999: '))

            # Отримуємо максимальне значення
            max = 0
            while max < min or max > 1000:
                max = int(input(f'Введіть МАКСимальне число в діапазоні від {min} до 1000: '))

            # Отримуємо значення кількості
            quantity = 0
            while quantity < 1 or quantity > (max-min+1):
                quantity = int(input(f'Скільки унікальних чисел генеруємо? Оберіть число між 1 та {max-min+1}: '))
            
            # Записуємо всі значення в об'єкт
            lottery_range = (min, max, quantity)
            
            return lottery_range

        except ValueError:
            print('Всі числа мають бути цілими (без коми) та написані цифрами. Спробуйте ще раз спочатку.\n')
            continue

def get_numbers_ticket() -> list:
    
    min, max, quantity = get_range()
    numbers = []
    population = []

    # Генерація та повернення списка чисел
    for num in range(min, max+1):
        population.append(num)
    
    numbers.extend(random.sample(population, quantity)) # чому тут не можна ланцюжком викликати .sort()?
    sorted_numbers = (sorted(numbers))
    print(f"Ваші {quantity} лотерейних числа(-ел) в межах від {min} до {max}:", sorted_numbers)
    
    return sorted_numbers

if __name__ == '__main__':
    get_numbers_ticket()