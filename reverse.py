#program to reverse a word

word = input("input a word to reverse:")

for char in range(len(word)-1,-1,-1):
  print(word[char],end="")
print('\n')