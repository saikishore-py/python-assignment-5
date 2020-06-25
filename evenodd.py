#python program to count even and odd numbers in a list

list1= [10,31,4,33,77,98]

even_count,odd_count = 0,0

#iteration each number in list

for num in list1:
  if num%2==0:
     even_count+=1
  else:
    odd_count+=1
print("even numbers in the list:",even_count)
print("odd numbers in the list:",odd_count)