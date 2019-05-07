import os

os.system('clear')

print ("Creating Configuration:\n")

print ("OSW1J03.ewr1\n")

count=1

for i in range (25,49):
    print ('int Gi0/' + str(i))
    print ('description xcoder' + str(count) + '.xxxx.xxxx')
    print ('switchport access vlan 306')
    print ('\n')
    count+=1

print ("OSW1J01.ewr1\n")

count2=25

for x in range (1,12):
    print ('int Gi0/' + str(x))
    print ('description xcoder' + str(count2) + '.xxxx.xxxx')
    print ('switchport access vlan 306')
    print ('\n')
    count2+=1
