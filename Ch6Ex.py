# Write for loops to accomplish each of the following tasks:

# # a. Print the numbers 0 - 20, one number per line.
# for char in range(21):
#     print(char)


# # b. Print only the ODD values from 3 - 29, one number per line.
# for num in range(3, 31, 2):
#     print(num)

# # c. Print the EVEN numbers 12 down to -14 in descending order, one number per line.
# for num in range(12, -16, -2):
#     print(num)

# d. Print the numbers 50 down to 20 in descending order, but only if the numbers are multiples of 3.


# for num in range(50, 20, -1):
#     if num % 3 == 0:
#         print(num)


## PART 2


word = 'LaunchCode'

# # Given the string in 'word' code for loops to do the following:

# # a) Print out each character of the string, one letter per line. Do this WITHOUT using index values.
# # for char in word:
# #     print (char)


# b) Use index values to print each character of the string—in reverse order—to a new line. To access a single character from a string, use the syntax word[index], where index is an integer value.

# num = len(word)

# for char in word:
#     print(word[num - 1])
#     num -= 1



### Part 3

# Code a for loop to print the every 5th character from 'gibberish', including the first character. Use index values and range(start, stop, step).
# Hint: Instead of figuring out the stop value by counting all of the characters in gibberish yourself, make Python do it for you! 
# len(gibberish) returns the length of the string stored in the variable..

# gibberish = 'Vna#hewzB*rQhT%yq^lv %PwgOexWo &C^oUoGSdtJLj'
# num = 5

# for char in gibberish:
#     if 


# Repeat this process, but replace range(start, stop, step) with range(len(gibberish)).
# Use an if statement and the modulus (%) operator to check if the index is divisible by 5. If True, print the character. If False, do not print the character.
# The output should be the same as before.



## While Practice

# Define three variables for a spacecraft - one for the starting fuel level, another for the number of astronauts aboard, and the third for the altitude the spacecraft reaches.

start_fuel_level = 0
number_of_astronauts = 0
alt = 0

# Code a while loop to ask the user for the starting fuel level. The loop should continue until the user enters a value between 5000 and 30000. If the user submits a number outside of the range, print "Invalid entry."
user = 0

while user <= 0:
    user = int(input('Enter fuel level: '))
    if user < 5000 or user > 30000:
        print('invalid number')



    


# Code a second loop to prompt the user for the number of astronauts. Have the loop continue until the user enters an integer from 1 - 7.



# Use a third while loop to update the fuel and the altitude of the spacecraft. Each iteration, decrease the fuel level by 100 units for each astronaut aboard. Also, increase the altitude by 50 kilometers. 
# The loop should end when there is not enough fuel to boost the crew another 50 km, so the fuel level might not reach 0.



# After the loops finish, print the result using the phrase, "The spacecraft gained an altitude of ___ km and has ___ kg of fuel left." Fill in the blanks with the current altitude and fuel level values.

# If the altitude is 2000 km or higher, add "Orbit achieved!" to the output. Otherwise add, "Failed to reach orbit."