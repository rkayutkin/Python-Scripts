###Take Duplicates out of a list###
a = [3, 4, 2, 2, 2, 1]
b=[]

for i in a:
    if i not in b:
        b.append(i)

print b

###Add Duplicates to a new list###

l = [3, 4, 2, 2, 2, 1]
f = []

for i in l:
    if l.count(i) > 1:
        f.append(i)

print f
