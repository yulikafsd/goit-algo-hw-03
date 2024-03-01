import re

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "38,050.123;4567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "8050-111-22-22",
    "38050 111 22 11   ",
]

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

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
