'''
Problem: Write a recursive function to find the sum of all natural numbers up to n.
sum_natural(5) -> 15 
'''

def sum_natural(n):
  # Base case (The simpliest cast)
  if n == 1:
    return 1 
  return n + sum_natural(n - 1)

print(sum_natural(10))