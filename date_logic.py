from datetime import datetime,timedelta
import math

def closest_number(n, m) -> int:
    q = math.ceil(n / m) 
    number = m * q
    return number


def last_day(d, day_name="sunday") -> datetime:
    days_of_week = ['sunday','monday','tuesday','wednesday',
                        'thursday','friday','saturday']
    target_day = days_of_week.index(day_name.lower())
    delta_day = target_day - d.isoweekday()
    if delta_day >= 0: 
        delta_day -= 7 # go back 7 days

    return d + timedelta(days=delta_day)


def find_start_date() -> datetime:
    date_today = datetime.today()
    date_year_ago = date_today - timedelta(days=358)
    sunday = last_day(date_year_ago, "sunday")
    return sunday


def get_dates(word, letters, start_date) -> list[datetime]:
    word = word.lower()
    letter_dates = []
    last_pos = 0
    
    for letter in word:
        last_pos = closest_number(last_pos, 7)
        
        if letter == " ":
            last_pos += 21
        else: 
            letter_arr = letters[letter]    
            for letter_pos in letter_arr:
                pos = letter_pos + last_pos
                letter_dates.append(start_date + timedelta(days=pos))
                
            last_pos += (letter_arr[-1] + 7) 

    return letter_dates