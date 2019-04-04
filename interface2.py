import os

os.system('clear')

print ("Creating Configuration:\n")

# [(x, y) for x in range(325,349) for y in range (1,25)]
#     print ('int po ' + str(x))
#     print ('description xcoder' + str(y))

# for x in range (1,25):
#     description= ('description xcoder' + str(x) + '.c01.xcode.file.clt2.prod')

count=25

print ("######Configuration for LEAF1######:\n")

for n in range (301,312):
    print ('int po ' + str(n))
    print ('description xcoder' + str(count) + '.c01.xcode.file.clt2.prod')
    print ('switchport')
    print ('switchport access vlan 3001')
    print ('spanning-tree port type edge')
    print ('no lacp suspend-individual')
    print ('vpc ' + str(n))
    print ('\n')
    count += 1

print ('\n')

count2=25
count3=301

for i in range (1,12):
    print ('int eth1/' + str(i))
    print ('description xcoder' + str(count2) + '.c01.xcode.file.clt2.prod-LAN-1')
    print ('switchport')
    print ('switchport access vlan 3001')
    print ('spanning-tree port type edge')
    print ('channel-group ' + str(count3) + ' mode active')
    print ('\n')
    count2 += 1
    count3 += 1

print ("######Configuration for LEAF2######:\n")

count4=25

for j in range (301,312):
    print ('int po ' + str(j))
    print ('description xcoder' + str(count4) + '.c01.xcode.file.clt2.prod')
    print ('switchport')
    print ('switchport access vlan 3001')
    print ('spanning-tree port type edge')
    print ('vpc ' + str(j))
    print ('\n')
    count4 += 1

print ('\n')

count5=25
count6=301

for k in range (1,12):
    print ('int eth1/' + str(k))
    print ('description xcoder' + str(count5) + '.c01.xcode.file.clt2.prod-LAN-2')
    print ('switchport')
    print ('switchport access vlan 3001')
    print ('spanning-tree port type edge')
    print ('channel-group ' + str(count6) + ' mode active')
    print ('\n')
    count5 += 1
    count6 += 1
