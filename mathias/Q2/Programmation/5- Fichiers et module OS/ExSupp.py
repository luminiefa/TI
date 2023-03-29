import os
#import shutil
#
#shutil.move("5- Fichiers et module OS/test.txt", "5- Fichiers et module OS/test/test.txt")

def lower_case(word) :
    lower_case_word = []
    i = 0
    while i < len(word) :
        if 65 <= ord(word[i]) <= 90 : 
            lower_case_word.append( chr(ord(word[i])+32) )
        else :  lower_case_word.append(word[i])
        i += 1
    return ''.join(lower_case_word)

if __name__ == "__main__" :

    with open ("5- Fichiers et module OS/lorem-ipsum.txt","r") as file :
        text = file.read()

    word_list = text.split()
    new_word_list = []
    for word in word_list :
        new_word_list.append(lower_case(word))
    word_list = new_word_list

    counted = []
    for word in word_list :
        if word not in counted :
            print(word,":",word_list.count(word))
            counted.append(word)
    