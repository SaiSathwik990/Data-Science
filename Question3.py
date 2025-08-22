'''
program to split, search and replace string using pattern matching and regular expression
'''

import re

source_text = input("Enter source text with special symbols to split, words to replace : ")

source = input("Enter which word to replace : ")
dest = input("Enter word to replace : ")
search = input("Enter word to search : ")

print()
words = re.split(r'[\s,]+', source_text)
print("Split words : "+str(words))

source_text = ' '.join(words)
source_text = re.sub(source, dest, source_text)
print("Replaced Text : "+source_text)

match = re.search(search, source_text)
if match:
    print("Search Result : "+str(match.group()))
else:
    print("Search string not found")
