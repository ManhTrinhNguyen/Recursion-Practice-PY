'''
Generate All Subsets of a String
Problem: Write a recursive function to generate all subsets (or subsequences) of a given string.

subsets("abc") -> ['', 'a', 'b', 'c', 'ab', 'ac', 'bc', 'abc'] 
subsets("xy") -> ['', 'x', 'y', 'xy'] 
'''
def subsets(str):
  # Base case 
  if str == '':
    return ['']
  
  # Recursive case: Get all subsets of the rest of the string
  smaller_subset = subsets(str[1:])

  new_subset = [] 
  for subset in smaller_subset:
    new_subset.append(subset)
    new_subset.append(str[0] + subset)
    
  return new_subset

print(subsets("abc"))