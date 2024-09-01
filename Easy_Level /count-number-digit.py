'''
  Count the Number of Digits in a Number
  Problem: Write a recursive function to count the number of digits in a given integer.

  count_digits(12345) -> 5 
  count_digits(7) -> 1 
'''

def count_digits(num):
  numStr = str(num)
  # Base case 
  if len(numStr) == 1 :
    return 1
  
  return 1 + count_digits(numStr.replace(numStr[0], "", 1))

print(count_digits(1))