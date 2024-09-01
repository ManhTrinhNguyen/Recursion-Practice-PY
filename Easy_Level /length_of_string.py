'''
  Problem: Write a recursive function to find the length of a given string.
  length("hello") -> 5 
  length("recursion") -> 9 
'''
def length(str):
  # Base Case 
  if str == "":
    return 0
  
  # Recursive Case 
  return 1 + length(str.replace(str[0], "", 1))

print(length("Hello"))
print(length("recursion"))