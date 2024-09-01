'''
  Problem: Write a recursive function to find the minimum element in an array.
  find_min([3, 5, 1, 8, 2]) -> 1 
  find_min([7, 2, 10, 4]) -> 2 
'''

def find_min(arr):

  # Base case . What is the simpliest case 
  if len(arr) == 1:
    return arr[0]

  # Recursive Case 
  if arr[0] < arr[1]:
    return find_min([arr[0]] + arr[2:]) # This will take out the arr[1]
  else:
    return find_min(arr[1:]) # This will take out the arr[0]

print(find_min([3, 5, 1, 8, 2]))
print(find_min([7, 2, 10, 4]))