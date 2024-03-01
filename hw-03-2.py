import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    
    numbers = []

    # Перевірка вірного формату аргументів
    try:
        # Якщо параметри не відповідають заданим обмеженням, функція повертає повідомлення.
        if min < 1 or min > 1000 or max < 1 or max > 1000:
            print('Для генерації унікальних чисел оберіть числа в діапазоні від 1 до 1000')
            return numbers
        
        elif quantity < min or quantity > max:
            print('Кількість згенерованих чисел не може бути менша за обраний Вами min та більша за обраний Вами max')
            return numbers
            
        # Генерація та повернення списку з вказаною кількістю унікальних чисел у заданому діапазоні.
        else:
            population = []
            for num in range(min, max+1):
                population.append(num)
            numbers.extend(random.sample(population, quantity)) # чому тут не можна ланцюжком викликати .sort()?
            sorted_numbers = (sorted(numbers))
            print("Ваші лотерейні числа:", sorted_numbers)
            return sorted_numbers

    except TypeError:
        print('Функція приймає лише цілі числа!')

get_numbers_ticket(1, 49, 6)

