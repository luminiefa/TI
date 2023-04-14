def dict_count(word):
    
    dictionary = {}
    letters = []

    for letter in word:
        letters.append(letter)

    i = 0
    while i < len(letters):
        dictionary.update(dict([(letters[i], letters.count(letters[i]))]))
        i += 1
        
    return dictionary


def nb_different_char(word):
    return len(dict_count(word))


word = "hello"
print(nb_different_char(word))
