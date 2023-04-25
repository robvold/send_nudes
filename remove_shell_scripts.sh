# Shell-script used to remove the generated files created by the python-script
# Run using, 'sh remove_shell_scripts.sh'

find -iname "*.sh" ! -name 'remove_shell_scripts.sh' |  xargs rm