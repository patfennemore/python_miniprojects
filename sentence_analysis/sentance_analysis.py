# Sentence Analysis Tool

# Write a script that takes a sentence from the user and returns:

# - the number of lower case letters
# - the number of uppercase letters
# - the number of punctuations characters
# - the total number of characters

# Use a dictionary to store the count of each of the above.

# **Note**: ignore all spaces.


sentence = input("Write a sentence :")

upper_case_count = 0
for upper_case in sentence:
     if(upper_case.isupper()):
         upper_case_count += 1

print("Upper case: " + str(upper_case_count))

lower_case_count = 0
for lower_case in sentence:
     if(lower_case.islower()):
         lower_case_count += 1

print("Lower case: " + str(lower_case_count))

punctuation_count = 0
for punc in range (0, len (sentence)):
     if sentence[punc] in ('!', "," ,"\'" ,";" ,"\"", ".", "-" ,"?"):
         punctuation_count += 1

print("Punctuation: " + str(punctuation_count))

character_count = len(sentence)
print("Total chars: " + str(character_count))

Dict = {"Upper case": upper_case_count, "Lower case": lower_case_count, "Punctuation": punctuation_count, "Total_chars":character_count}
