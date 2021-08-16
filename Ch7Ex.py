wordb = "Strings are squences of characters."
print(wordb[0:12])


num = len(wordb)

print(wordb[num - 12 : num] )

num2 = len(wordb)//2

print (wordb[num2 - 6: num2 + 6])

print (wordb[0])

num = 1001

# Throws an error:
# print(len(num))

# Use type conversion to print the length (number of digits) of an integer.
print (len(str(num)))


# Follow up: Print the number of digits in a DECIMAL value (e.g. num = 123.45 has 5 digits but a length of 6).




# Experiment! What if num could be EITHER an integer or a decimal?  Add an if/else statement so your code can handle both cases.