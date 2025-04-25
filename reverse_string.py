#The function to reverse a string manually
def reverse_string(s):
reversed_str = ""
for char in s:
   reversed_str = char + reversed_str #Add character in front
return reversed_str
#Example
print(reverse_string("welcome")) #Output:emoclew
