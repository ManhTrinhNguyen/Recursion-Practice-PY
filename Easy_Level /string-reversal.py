def string_reversal(str):
  # Base case 
  if len(str) == 0:
    return ''
  # What is smallest amount of work in each iteration ?
  return string_reversal(str.replace(str[0], '', 1)) + str[0]

'''
  string(hien)
  n + hie 
  n + e + hi
  n + e + i + h 
  n + e + i + h + ''
'''
  
print(string_reversal('hien'))

hien = 'hien'
print(hien.replace(hien[0], '', 1))
