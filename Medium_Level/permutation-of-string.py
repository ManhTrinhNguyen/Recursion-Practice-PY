'''
Problem: Write a recursive function to generate all permutations of a given string.
Input: "ABC"
Output:
ABC
ACB
BAC
BCA
CAB
CBA
'''

def permutation_of_string(str):
  # Base case : When string has only 1 character return that str
  if len(str) == 1:
    return [str] 
  
  # List to store permutation 
  permutation = []
  
  for i in range(len(str)):
    # Remove the character at index i and get the remaining string
    remaining_str = str[:i] + str[i+1:]

    # Recursively get all permutations of the remaining string
    for perm in permutation_of_string(remaining_str):
      # Add the removed character to each permutation of the remaining string
      permutation.append(str[i] + perm)

  return permutation


print(permutation_of_string('abcd'))

