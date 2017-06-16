import subprocess as sp
# subprocess module is used to run commands of shell...
# in python script.

# to take screen shot via shell
# import -window root screen.png
sp.call(["import", "-window", "root", "screen.png"])
