import os

filename = "ip.txt"
file = open(filename, "r")
for line in file:
    response = os.system("ping -t 2 " + line)
    if response == 0:
        print
        print line, 'IS UP!!!'
        print
    else:
        print
        print line, 'IS DOWN!!!'
        print
