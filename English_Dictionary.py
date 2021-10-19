# import library
import json
from difflib import get_close_matches

# load up the Dictionary Data from json file, Open json file in read mode only
data = json.load(open("data.json", "r"))

def translate(word):
    '''This function takes in String as input and returns the list of corresponding translations of that word 
    if that word exists in dictionary'''
    word = word.strip()
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys(), 5)) > 0:
        yn = input("Did you mean \'{}\' instead? If yes enter \'Y\' else enter \'N\'\n".format(get_close_matches(word, data.keys())[0]))
        if yn == 'Y':
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == 'N':
            return "{} does not exist. Kindly check it".format(word)
        else:
            return "We doesn\'t understand your entry :) "
    else:
        return "{} does not exist. Kindly check it".format(word)

# User Input 
word = input("Enter word to search: ")

# Output section
output = translate(word)

if type(output) == list:
    i = 1
    for item in output:
        print("{}  {}.".format(i, item))
        i += 1
else:
    print(output)