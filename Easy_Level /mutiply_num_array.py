'''
  Calculate the Product of an Array
  Problem: Write a recursive function to calculate the product of all elements in an array.
  
  product([1, 2, 3, 4]) -> 24 
  product([5, 6, 7]) -> 210 
'''

def product(arr):
  # Base case
  if len(arr) == 1: 
    return arr[0]
  # Recursive case
  return arr[0] * product(arr[1:])  

print(product([5, 6, 7]))
print(product([1, 2, 3, 4]))