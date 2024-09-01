'''
Problem: Write a recursive function to count the number of occurrences of a character in a string.
count_occurrences("hello", 'l') -> 2 
count_occurrences("recursion", 'r') -> 2 
'''

def count_occurrences(str, occurence):
  # Base case . Consider simplest scenario 
  if str == '':
    return 0
  
  if str[0] == occurence:
    return 1 + count_occurrences(str.replace(str[0], '', 1), occurence)
  else :
    return count_occurrences(str.replace(str[0], '', 1), occurence)

  
  
print(count_occurrences("hello", 'l'))
# Base case 
# Create a count to keep track how many time it occurence 
# 