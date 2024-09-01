'''
Problem: Write a recursive function to find the GCD of two numbers.
Input: a = 56, b = 98
Output: 14
'''

def greatest_common_divisor(a, b):
  if b == 0: 
    return a
  return greatest_common_divisor(b, a%b)
  


print(greatest_common_divisor(56, 98))