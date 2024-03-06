import re
from data import raw_numbers

def normalize_phone(phone_number: str):
    
    # видаляє всі символи, крім цифр та символу '+'
    pattern = r"[a-zA-Z;,:!()\-\.\s\\]"
    repl = ''
    norm_phone = re.sub(pattern, repl, phone_number)
    
    # додає код '+38'
    # Чи можна тут використати match - case замість if - elif - else та як саме?
    if norm_phone.startswith('+380'):
        return norm_phone
    elif norm_phone.startswith('380'):
        return '+' + norm_phone
    elif norm_phone.startswith('80'):
        return '+3' + norm_phone
    elif norm_phone.startswith('0'):
        return '+38' + norm_phone
    else:
        return '+380' + norm_phone    

def sanitized_numbers(phone_numbers):
    sanitized_numbers = [normalize_phone(num) for num in phone_numbers]
    print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
    return sanitized_numbers

if __name__ == '__main__':
    sanitized_numbers(raw_numbers)
