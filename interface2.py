import os

os.system('clear')

print ("Creating Configuration:\n")

count=25

print ("######Configuration for LEAF1######:\n")

for n in range (301,312):
    print ('int po ' + str(n))
    print ('description xcoder' + str(count) + '.xxxx.xxxx')
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
    print ('description xcoder' + str(count2) + '.xxxx.xxxx')
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
    print ('description xcoder' + str(count4) + '.xxxx.xxxx')
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
    print ('description xcoder' + str(count5) + '.xxxx.xxxx')
    print ('switchport')
    print ('switchport access vlan 3001')
    print ('spanning-tree port type edge')
    print ('channel-group ' + str(count6) + ' mode active')
    print ('\n')
    count5 += 1
    count6 += 1
