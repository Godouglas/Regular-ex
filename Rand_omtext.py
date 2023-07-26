import os
import re

text = open("123.txt", "r")

pattern = input("Enter word you want to find: ")
repl_ace = input("Enter word to replace: ")
x = text.read()

y = re.search(pattern, x)
if y:
    y = re.sub(pattern, repl_ace, x)
    print(y)
else:
    print("Word not found")
text.close()
