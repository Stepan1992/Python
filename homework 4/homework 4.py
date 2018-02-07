#task_1

key = 'aaaaabbbbbabbbaabbababbaaababaab'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
text = str(input("Enter a cipher "))
cipher = ''
uncipher = ''
i = 0

for letter in text:
    if letter == ' ':
        continue
    if letter == letter.lower():
        cipher = cipher + 'a'
    else:
        cipher = cipher + 'b'

remnant = len(cipher) % 5

if remnant != 0:
    cipher = cipher[0 : len(cipher) - remnant]

def decipher():
    result = ""
    j = 0
    z = 5 
    while z <= len(cipher):
        unit = cipher[j : z]
        alphabet_element = key.find(unit)
        j = j + 5
        z = z + 5
        result = result + alphabet[alphabet_element]
    
    return result

print(decipher())

# task 2

import math
string = input("Enter a palindrome ")
partsLentgth = math.ceil(len(string) / 2)

def palindromeCkeck():
    i = 0
    while i < partsLentgth:
        if string[i] != string[len(string) - i - 1]:
            return "false"      
        return "true"

print(palindromeCkeck())
