# find the most repeated character in this text
# first need to know how many times each character is repreated then find the most repeated character
# use a dictionary data structure to store this info because its a collection of key value paris
# characters as keys a repetiton as the value

from pprint import pprint
sentence = "This is a common question in the tech field"

char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

char_frequency_sorted = sorted(
    char_frequency.items(),
    key=lambda kv: kv[1],
    reverse=True)

print(char_frequency_sorted[0])
