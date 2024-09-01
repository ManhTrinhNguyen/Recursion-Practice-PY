'''
  Sum of Elements in an Array
  Problem: Write a recursive function to find the sum of all elements in an array.
  sum_array([1, 2, 3, 4, 5]) -> 15 
  sum_array([10, 20, 30]) -> 60 
'''

def sum_array(arr):
  # Base case 
  if len(arr) == 1:
    return arr[0]
 
  # Recursive 
  return arr[len(arr) - 1] + sum_array(arr[:-1])

print(sum_array([10, 20, 30]))
print(sum_array([1, 2, 3, 4, 5]))