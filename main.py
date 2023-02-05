from datetime import datetime,timedelta
import time

def last_day(d, day_name):
    days_of_week = ['sunday','monday','tuesday','wednesday',
                        'thursday','friday','saturday']
    target_day = days_of_week.index(day_name.lower())
    delta_day = target_day - d.isoweekday()
    if delta_day >= 0: delta_day -= 7 # go back 7 days
    return d + timedelta(days=delta_day)


def create_file(word) -> None:
    f = open("example.sh", "w")
    f.write("Now the file has more content!")
    f.close()




def main():
    print("test:")
    date_today = datetime.today()
    print(last_day(date_today, "sunday"))
    create_file("tst")

main()