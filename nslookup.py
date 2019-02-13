import subprocess

hfile= open("hostnames.txt", "r")

main= {'key':'value'}

for i in hfile:
    grep1= " | awk '{print $5}'"
    grep2= " | grep -P '\b([0-9]{1,3}\.){3}[0-9]{1,3}\b'"
    lookup= 'nslookup ' + i + grep1
    output= subprocess.check_output(lookup, shell=True)
    print (output)

hfile.close()
