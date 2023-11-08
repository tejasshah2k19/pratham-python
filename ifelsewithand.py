#and 

#take three numbers and find out max 

print("Enter three numbers")
n1 = input()
n2 = input()
n3 = input()

n1 = int(n1)
n2 = int(n2)
n3 = int(n3)

if n1 > n2 and n1 > n3: 
    print("n1 is max")
elif n2 > n1 and n2 > n3:
    print("n2 is max")
else:
    print("n3 is max")
    