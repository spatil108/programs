
######### Unique Element in an array ##########

x = []

z = int(input("How many items in list: "))

while len(x) < z:
    y=input("Enter items in list.")
    x.append(y)

print(x)


output = []

for i in range(len(x)):
    if x[i] not in output:
        output.append(x[i])

print(output)
