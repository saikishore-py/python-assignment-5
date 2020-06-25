#program to find fibonacci series

nt= int(input("no of terms terms:"))

n1, n2 = 0, 1
count=0

if nt<= 0:
   print("please enter the positive integer")
elif nt == 1:
   print("fibonnaci sequence upto",nt,':')
   print(n1)
else:
   print("fibonnaci sequence:")
   while count < nt:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count+= 1