import subprocess
import os

wd= raw_input("Please enter the full directory path you would like to find '.txt' files in: ")

os.chdir(wd)
os.getcwd()
command= "ls | grep .txt || true"
doutput= subprocess.check_output(command, shell=True)

print doutput
