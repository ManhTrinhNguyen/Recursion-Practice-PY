'''
  Fibonacci number : 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610,....
    The 0th Fibonacci number is 0.
    The 1st Fibonacci number is 1.
    The 2nd Fibonacci number is 1 (0 + 1).
    The 3rd Fibonacci number is 2 (1 + 1).
    The 4th Fibonacci number is 3 (1 + 2).
    The 5th Fibonacci number is 5 (2 + 3)
    The 6th Fibonacci number is 8 (3 + 5)
'''

 
def fibonacci(n):
  # Base case 
  if n <= 1:
    return n
  return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(20))