#program for converting binary number to decimal value



binary= list(input("enter the binary number"))

value=0
for i in range (len(binary)):
    digit= binary.pop()
    if digit =='1':
        value = value+pow(2,i)
print("the decimal value of the binary number is:", value)