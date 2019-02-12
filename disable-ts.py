#This is a script to disable Touch Screen in Ubuntu

import subprocess

#find_id= "xinput | grep Touchscreen | sed 's/.*id=\([0-9]*\).*/\1/'"

#First grep only matches the line with "Tochscreen" in it
#Second grep matches "id=and the digits"
#Third grep finally only takes that digit we need to disable our Touchscreen
find_id= "xinput | grep Touchscreen | grep -Eo '(id=)[0-9]{1,4}' | grep -o '[0-9]*'"
result= subprocess.check_output(find_id, shell=True)

disable= "xinput disable " + result
subprocess.call(disable, shell=True)

print ("The script has successfuly disabled xinput " + result)
