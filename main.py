from date_logic import *
from letters import letters


def create_file(dates) -> None:
    f = open("commit.sh", "w")
    file_content = "git add .\n"
    for _ in range(7):
        for date in dates:
            file_content += "GIT_AUTHOR_DATE=\"" + str(date) + "\" GIT_COMMITTER_DATE=\"" + str(date) + "\" git commit --allow-empty -m \"important work\" > /dev/null\n"
    file_content += "git push\n"
    f.write(file_content)
    f.close()


def main():
    start_date = find_start_date()
    calendar_word = "send nudes"
    dates_for_word = get_dates(calendar_word, letters, start_date)
    create_file(dates_for_word)

    print("Created shell file")


main()

