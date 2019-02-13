import subprocess

hfile= open("hostnames.txt", "r")
hostnames=[]

main= {'key':'value'}

for i in hfile:
    hostnames.append(i)

for i in hostnames:
    grep1= " | awk '{print $5}'"
    grep2= " | grep -P '\d.*[0-9]\d.*.'"
    lookup= 'dig ' + i + grep1 + grep2
    output= subprocess.check_output(lookup, shell=True)
    print (output)

hfile.close()
