'''
  Problem: Write a recursive function to find the maximum element in an array.
 
  find_max([1, 5, 3, 9, 2]) -> 9 
  find_max([4, 2, 7, 1]) -> 7 
'''

def find_max(arr):
   # Base Case 
  if len(arr) == 1:
    return arr[0]
  
  # Recursive Case 
  if arr[0] < arr[len(arr) - 1]:
    return find_max(arr[1:])
  else: 
    return find_max(arr[:-1])
  

  
print(find_max([1, 5, 3, 9, 2]))
print(find_max([4, 2, 7, 1]))
  