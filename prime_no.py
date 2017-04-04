
#######  Prime No  #######

x = int(input("Enter the Number to check for the prime number test ?"))

for i in range(2, (x/2)):
	if (x%i==0):
	        print ("%d is not the prime number" % (x))
		break

else:
	print("%d is prime" % (x))





