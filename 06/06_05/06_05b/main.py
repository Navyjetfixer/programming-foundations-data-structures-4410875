from collections import deque

def matching_para(text):
  stack = deque()
  for char in text:
   if char == '(':
     stack.append(char)
     
   elif char == ')':
     if not stack:
       return False
     stack.pop()
     
    
  
  return len(stack) == 0  
      
    
      
  
print(matching_para(')(hi )there)('))
