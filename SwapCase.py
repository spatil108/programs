s = input()
a = list(s)

print(a)
    
for i in range(len(a)):
    if (a[i].isupper()): """Or if (a[i] == a[i].upper):"""
        a[i]=a[i].lower()
    else:
        a[i]=a[i].upper()

print(a)

    
