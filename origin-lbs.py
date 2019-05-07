import os

os.system('clear')

print ("Creating Configuration:\n")

count=1

print ("######Configuration for BLEAF1######:\n")

for n in range (321,325):
    print ('int po ' + str(n))
    print ('description LB' + str(count) + 'XXXX')
    print ('switchport')
    print ('switchport mode trunk')
    print ('no lacp suspend-individual')
    print ('vpc ' + str(n))
    print ('\n')
    count += 1

print ('\n')

count2=1
count3=321

for i in range (21,25):
    print ('int eth1/' + str(i))
    print ('description LB' + str(count2) + 'XXXX')
    print ('switchport')
    print ('switchport mode trunk')
    print ('spanning-tree port type edge')
    print ('channel-group ' + str(count3) + ' mode active')
    print ('no shut')
    print ('\n')
    count2 += 1
    count3 += 1

print ("######Configuration for BLEAF2######:\n")

count4=1

for j in range (321,325):
    print ('int po ' + str(j))
    print ('description LB' + str(count4) + 'XXXX')
    print ('switchport')
    print ('switchport mode trunk')
    print ('spanning-tree port type edge')
    print ('vpc ' + str(j))
    print ('\n')
    count4 += 1

print ('\n')

count5=1
count6=321

for k in range (21,25):
    print ('int eth1/' + str(k))
    print ('description LB' + str(count5) + 'XXXX')
    print ('switchport')
    print ('switchport mode trunk')
    print ('spanning-tree port type edge')
    print ('channel-group ' + str(count6) + ' mode active')
    print ('no shut')
    print ('\n')
    count5 += 1
    count6 += 1

print ("######Configuration for ERT1######:\n")

count7=1

for i in range (21,25):
    print ('int Eth0/' + str(i))
    print ('description LB' + str(count7) + 'XXXX')
    print ('switchport')
    print ('switchport mode access')
    print ('switchport access vlan 290')
    print ('spanning-tree port type edge')
    print ('shut')
    print ('\n')
    count7+=1

print ("######Configuration for ERT2######:\n")

count8=1

for i in range (21,25):
    print ('int Eth0/' + str(i))
    print ('description LB' + str(count8) + 'XXXX')
    print ('switchport')
    print ('switchport mode access')
    print ('switchport access vlan 291')
    print ('spanning-tree port type edge')
    print ('shut')
    print ('\n')
    count8+=1
