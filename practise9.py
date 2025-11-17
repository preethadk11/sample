import re
letter="Python is 1 1good"
letter_count=re.sub("[^a-zA-Z]","",letter)
digit_count=re.sub("[^0-9]","",letter)
print(len(letter_count))
print(len(digit_count))