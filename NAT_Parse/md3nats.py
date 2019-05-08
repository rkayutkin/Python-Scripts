external= open("EXTERNAL.txt", "r")
internal= open("INTERNAL.txt", "r")

print

print ("These are the object commands for internal object-groups:\n")
for i in internal:
    internal2= i.strip()
    print("show object-group id "+ internal2)

print

print ("These are the object commands for external object-groups:\n")
for i in external:
    external2= i.strip()
    print("show object-group id "+ external2)
