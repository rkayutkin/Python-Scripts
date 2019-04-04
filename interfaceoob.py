import os

os.system('clear')

print ("Creating Configuration:\n")

# [(x, y) for x in range(325,349) for y in range (1,25)]
#     print ('int po ' + str(x))
#     print ('description xcoder' + str(y))

# for x in range (1,25):
#     description= ('description xcoder' + str(x) + '.c01.xcode.file.clt2.prod')

print ("OSW1J03.ewr1\n")

count=1

for i in range (25,49):
    print ('int Gi0/' + str(i))
    print ('description xcoder' + str(count) + '.c01.xcode.file.clt2.prod-OOB')
    print ('switchport access vlan 306')
    print ('\n')
    count+=1

print ("OSW1J01.ewr1\n")

count2=25

for x in range (1,12):
    print ('int Gi0/' + str(x))
    print ('description xcoder' + str(count2) + '.c01.xcode.file.clt2.prod-OOB')
    print ('switchport access vlan 306')
    print ('\n')
    count2+=1
