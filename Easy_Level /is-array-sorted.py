'''
  Problem: Write a recursive function to check if an array is sorted in ascending order.

  is_sorted([1, 2, 3, 4, 5]) -> True 
  is_sorted([5, 3, 2, 1]) -> False 
'''

def is_sorted(arr):
  # Base case 
  if len(arr) == 1:
    return True 
  
  if arr[0] + 1 == arr[1]:
    return is_sorted(arr[1:])
  
  return False 
  
print(is_sorted([1, 2, 6, 4, 5]))
print(is_sorted([5, 3, 2, 1]))
