from date_logic import *
from letters import letters
from argparse import RawTextHelpFormatter
import argparse
import traceback


def create_file(dates) -> None:
    f = open("commit.sh", "w")
    file_content = "git add .\n"
    for _ in range(7):
        for date in dates:
            file_content += "GIT_AUTHOR_DATE=\"" + str(date) + "\" GIT_COMMITTER_DATE=\"" + str(date) + "\" git commit --allow-empty -m \"important work\" > /dev/null\n"
    
    file_content += "git push\n"
    f.write(file_content)
    f.close()
    

def run(calendar_word):
    if not calendar_word:
        calendar_word = "send nudes"

    start_date = find_start_date()
    dates_for_word = get_dates(calendar_word, letters, start_date)
    create_file(dates_for_word)
    print("Created shell file")
 

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="\tScript for writing text to your commit history calendar.\n\tWill write \"send nudes\" if -t (text) is omitted", 
        formatter_class=RawTextHelpFormatter)
    parser.add_argument("-t", "--text", type=str, help="desired string to be created in the commit history calendar")
    args = parser.parse_args()

    try:
        run(args.text)
    except KeyError as e:
        err_msg = "Unable to generate shell file:\nLetter \"{}\" is not yet supported"
        print(err_msg.format(e.args[0]))
    except Exception as e:
        err_msg = "Unable to generate shell file:\n{}"
        print(err_msg.format("".join(traceback.format_exception(type(e), e, e.__traceback__))))
    


