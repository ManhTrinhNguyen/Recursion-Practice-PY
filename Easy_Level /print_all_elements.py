'''
  Problem: Write a recursive function to print all elements of an array.
 
  print_array([1, 2, 3, 4]) 
  Output: 1 2 3 4 
'''

def print_array(arr):
  # Base case
  if len(arr) == 0:
    return 
  
  print(arr[0])
  
  # Recursive case
  return print_array(arr[1:]) 

print(print_array([1, 2, 3, 4]))