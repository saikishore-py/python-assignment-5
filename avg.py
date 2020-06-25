#python program to find average of N natural number

number = int(input("enter the number:"))

total = 0
for value in range(1, number+1):
    total= total+value
    average = total/number
print("the avg of number 1 to {0} is {1}".format(number,average))