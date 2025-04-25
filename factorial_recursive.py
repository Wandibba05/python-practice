#The function to compute factorial using recursion
def factorial_recursive(n):
  if n==0 or n==1:
    return 1 # Base case
return n * factorial_recursive(n-1) #Recursive step

#Example
print(factorial_recursive(7)) #Output: 5040
