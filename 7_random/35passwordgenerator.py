# import random

# list1 = ["a","s","d","f","g","H","J","K","L","z","x","c","v","b","n","m"]
# list = [ 
# "A" "B" "C" "D" "E" "F" "G" "H" "I" "J" "K" "L" "M" "N" "O" "P" "Q" "R" "S" "T" "U" "V" "W" "X" "Y" "Z" "a" "b" "c" "d" "e" "f" "g" "h" "i" "j" "k" "l" "m" "n" "o" "p" "q" "r" "s" "t" "u" "v" "w" "x" "y" "z" "0" "1" "2" "3" "4" "5" "6" "7" "8" "9" "~" "" "!" "@" "#" "$" "%" "^" "&" "*" "(" ")" "_" "-" "+" "=" "{" "}" "[" "]" "|" "" ":" ";" "'" "<" ">" "," "." "?" "/"]

# password = random.choice(list)
# print(password)



import random
import string

all_characters = string.ascii_letters + string.digits + string.punctuation

password_length = int(input("Enter the desired password length: "))
print()
# Generate the password by randomly selecting characters
# random.choices returns a list, so we join it into a string
generated_password = ''.join(random.choices(all_characters, k=password_length))
print(all_characters)
print()
# Print the generated password
print("Your generated password is:", generated_password)