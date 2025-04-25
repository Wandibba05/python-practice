#The function to sum digits of a number
def sum_of_digits(n):
total = 0:
while n > 0:
  total += n % 10 #Add last digit
  n = n//10 #Remove last digit
return total
#Example
print(sum_of_digits(5678)) #Output is 26
