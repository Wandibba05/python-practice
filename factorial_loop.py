# The function to compute the factorial using a loop
def factorial_loop(n):
  result 1 # we start with 1 because it doesnt affect multiplication and it gives correct factorial
  for i in range(1,n +1):
    result *= i # Multiply the result by 1 each time
    return result

#Example
print(factorial_loop(7)) #Output is 5040
