![send_nudes](/send_nudes_github_calendar_text.png)

_**send_nudes**_: A simple tool for writing text to your commit history calendar. 

It works for both Github and Gitlab, Unix and Windows. It supports most of the ascii character set, including all the capital letters, and the most commonly used special characers. For a complete list, look at the `letters.py`-file. There is no limits to the length of the text printed.

It works by creating a shell-script, that uses gits ability to make commits in the past.

While testing the code you will probably generate a few `.sh`-files, you can use the provided `remove_shell_scripts.sh`-script to delete them all safely.

**Note**: It's recomended to execute the generated script in a empty repo as it will be easier to make changes later on.

<br>

## Usage
First you need to clone the repo:
``` bash
git clone https://github.com/robvold/send_nudes
```

Then you are able to use the tool with this general flow: 
1. Run the code
2. Move the created shell script to the desired repo
    a. Preferably an empty one
3. Execute the shell-script

### Commands
There are primarily two ways of running the code. You can make it print the default text, "send nudes", by running: 
``` bash
python send_nudes.py
```
You can also define the text with the `-t` or `-m` flag, like this:
``` bash
python send_nudes.py -t "some text"
```
If you need help use the `-h` flag:
``` bash
python send_nudes.py -h
```

### Removing the text
As the text is actually commits in a repo, the simplest way of deleting the text would be to delete the repo.

<br>

## License
_send_nudes_ is released under the GPL v3 license.

## Wanting to contribute?
Do you find a bug, miss a character or simply want to extend the functionality?
Feel free to make an PR or create an issue.