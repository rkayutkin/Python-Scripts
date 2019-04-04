import subprocess
import os

pwd= "/Users/roman.kayutkin"
os.chdir(pwd)

os.getcwd()
doutput= subprocess.check_output("ls | grep .txt", shell=True)

print doutput
