from datetime import date, datetime

users = [
    {"name": "John Doe", "birthday": "1985.03.03"},
    {"name": "Jane Smith", "birthday": "1990.03.06"}
]

def get_upcoming_birthdays(users: list) -> list:
    upcoming_bd_users = []
    current_date = date.today()

    for user in users:
        user_bd = datetime.strptime(user['birthday'], '%Y.%m.%d').date()
        this_year_bd = date(current_date.year, user_bd.month, user_bd.day)

        is_coming = current_date < this_year_bd
        is_next_week = (this_year_bd - current_date).days < 7
        
        # визначення днів народження на 7 днів вперед:
        if is_coming and is_next_week:
            
            # Обробка випадків, коли дні народження припадають на вихідні:
            bd_weekday = this_year_bd.weekday()
            
            match bd_weekday:
                case 5:
                    congrat_date = date(current_date.year, user_bd.month, (user_bd.day + 2))
                case 6:
                    congrat_date = date(current_date.year, user_bd.month, (user_bd.day + 1))
                case _:
                    congrat_date = this_year_bd
            
            congrat_date_string = congrat_date.strftime('%Y.%m.%d')
            bd_user = {'name' : user['name'], 'congratulation_date': congrat_date_string}
            upcoming_bd_users.append(bd_user)
    
    return upcoming_bd_users


upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)