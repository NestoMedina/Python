# user_entry = input('Enter a word: ')

# # 1) If the user's entry is longer than 5 characters, print "Your entry is longer than 5 characters!" Otherwise, print nothing.
# if len(user_entry) > 5:
#     print("Your entry is longer than 5 characters!")


# # 2) If the number entered by the user is 100 or larger, print "Valid entry!"  Otherwise, print, "Number too small."
# num_entry = int(input('Enter a number larger than 100: '))
# if num_entry >= 100:
#     print("Valid Entry!")
# else:
#     print("Number too small.")



# 3) Prompt the user to enter a lowercase letter. Use the 'in' operator to check if the letter is a vowel (e.g. in the string 'aeiou'). If so, print, "___ is a vowel." Else, print, "___ is NOT a vowel."
# # user_letter = input('Enter a lowercase letter: ')
# vowels = 'aeiou'
# up_vowels = "AEIOU"

# if user_letter in vowels or user_letter in up_vowels:
#     print (user_letter +" is a vowel.")
# else:
#     print (user_letter + " is NOT a vowel.")



# 4) What happens if the user enters a capital letter instead of lowercase? Refactor your code for problem 3 so that it works for both capital and lowercase vowels!


# _________________Part B______________________________________________________________________________________+++++++++++++++++++++++++++__+_+_++++++++++++++++++++++++++

# # 1) Given an integer, check to see if the number is even and divisible by 5. Print an appropriate message depending on the result.
# user_entry = int(input("Enter a whole number: "))

# if (user_entry % 5 == 0):
#     print("your number is even and divisible by 5")


# 2) Given a string, print, "___ is a really long word!" if the string is longer than 9 characters and does NOT contain a space. Otherwise, print, "___ is either short, or it contains multiple words." Fill in the blank with the original string.
test_string_1 = 'bookkeepers'
test_string_2 = 'Apricots and apples'
test_string_3 = 'carrot'
test_string_4 = 'apple pie'

if len(test_string_1) > 9 and ' ' not in test_string_1:
    print(test_string_1 + " is a really long word!")
else:
    print(test_string_1 + " is either short, or it contains multiple words.")



# 3) Refactor the following code to check if 'letter' is NOT in the string 'BCDFGHJKLMNPQRSTVWXYZ' or is a lowercase vowel. How does making this change affect the if/else code blocks?
letter = 'A'
cap_consonants = 'BCDFGHJKLMNPQRSTVWXYZ'
vowels = 'aeiou'

if letter not in cap_consonants or letter not in vowels:
  print("'" + letter + "'", "is either a lowercase vowel OR a capital consonant.")
else:
  print("Pick a capital consonant or a lowercase vowel")

# 4) Indicate whether each of following expressions returns True or False.
num = 5

if num >= 0 and num*2 <= 50 and num%2 == 0:
  print("This true")


num >= 0 or num*2 <= 50 or num%2 == 0
num >= 0 and num*2 <= 50 or num%2 == 0
num >= 0 or num*2 <= 50 and num%2 == 0
not num < 0 and num%3 != 0
not (num%3 == 0 or num*4 >= 20)