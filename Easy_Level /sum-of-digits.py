'''
  Problem: Write a recursive function to find the sum of the digits of a number.
  Input: 456
  Output: 15
'''
def sum_of_digits(num):
  # Turn number into str
  num = str(num)

  # base case 
  if len(num) == 0: 
    return 0
  return sum_of_digits(num.replace(num[0], '', 1)) + int(num[0])

print(sum_of_digits(777))