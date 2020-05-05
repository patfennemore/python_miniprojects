sentence = input("Write a sentence :")

# For each letter in the sentence , check the following
# if letter is a lower case add 1 to variable lowercase
# if letter is an upper case add 1 to variable uppercase
# if letter is a symbol from symbols add 1 to variable punctuation
# Add 1 to variable total_characters

letter_lowercase = 0
letter_uppercase = 0
punctuation_count = 0
total_characters = 0

# import string
# symbols = string.punctuation

for letter in sentence:
    if letter.islower():
        letter_lowercase += 1
    if letter.isupper():
        letter_uppercase += 1
    if letter == "!" or letter == "?" or letter == ",":
        punctuation_count += 1


print(letter_lowercase)
print(letter_uppercase)
print(punctuation_count)
print(total_characters)
