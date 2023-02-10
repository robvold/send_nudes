from datetime import datetime,timedelta
import time

def last_day(d, day_name) -> datetime:
    days_of_week = ['sunday','monday','tuesday','wednesday',
                        'thursday','friday','saturday']
    target_day = days_of_week.index(day_name.lower())
    delta_day = target_day - d.isoweekday()
    if delta_day >= 0: delta_day -= 7 # go back 7 days
    return d + timedelta(days=delta_day)

def find_start_date() -> datetime:
    date_today = datetime.today()
    date_year_ago = date_today - timedelta(days=365)
    sunday = last_day(date_year_ago, "sunday")
    return sunday


def get_dates(letter, start_date) -> list[datetime]:
    letter_dates = []
    for pos in letter:
        letter_dates.append(start_date + timedelta(days=pos))
    return letter_dates


letter_s = [6,13,20,23,24,27,29,32,33,35,42]

def create_file(dates) -> None:
    f = open("example.sh", "w")
    file_content = "git add .\n"
    for i in range(7):
        for date in dates:
            file_content += "GIT_AUTHOR_DATE=\"" + str(date) + "\" GIT_COMMITTER_DATE=\"" + str(date) + "\" git commit --allow-empty -m \"important work\" > /dev/null\n"
    file_content += "git push\n"
    f.write(file_content)
    f.close()

def main():
    start_date = find_start_date()
    dates_for_letter = get_dates(letter_s, start_date)
    create_file(dates_for_letter)

    print("Created shell file")
main()