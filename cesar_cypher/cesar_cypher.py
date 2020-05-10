secret = "I hear the gooseberries are doing well this year, and so are the mangoes."
cipher = 7

secret_letters_list = secret.lower().split()
secret_letters = []

for word in secret_letters_list:
    word = word + ' '
    for letter in word:
        secret_letters.append(letter)

dict_alphabet = {}
dict_cipher = {}
count = 0

import string
for letter in string.ascii_lowercase:
    cipher += 1
    dict_alphabet[letter] = count
    count += 1
    if cipher >= 26:
        dict_cipher[letter] = (cipher - 26)
    else:
        dict_cipher[letter] = cipher

cipher_numbers_list = []

for letter_cipher in secret_letters:
    for dict_cipher_letter, dict_cipher_number in dict_cipher.items():
        if letter_cipher == ' ':
            cipher_numbers_list.append(' ')
        else:
            cipher_numbers_list.append(dict_cipher.get(letter_cipher))
        break

cipher_code = []

for number in cipher_numbers_list:
    for dict_alphabet_letter, dict_alphabet_number in dict_alphabet.items():
        if number == dict_alphabet_number:
            cipher_code.append(dict_alphabet_letter)
    if number == " ":
        cipher_code.append(" ")

cipher_code_result = "".join(cipher_code)
print(cipher_code_result)
