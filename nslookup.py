import subprocess

hfile= open("hostnames.txt", "r")

main= {}

for i in hfile:
    # remove any ending spaces with srrip for the elements
    hfile2= i.strip()
    # parse for column 5
    grep1= " | awk '{print $5}'"
    # Regex i managed to get working to parse the IP addresses
    grep2= " | grep -E '\d.*[0-9]\d.*.'"
    # concatenating to build the command.
    lookup= "dig " + hfile2 + grep1 + grep2
    # Running the command with subprocess using shell, not safe.
    output= subprocess.check_output(lookup,shell=True)
    # Add a " , " between the output and create a new variable 
    output2= " , ".join(output.split())
    # Add the output from hile2 to Key and output2 to Value
    main[hfile2]= [output2]

print main

hfile.close()

