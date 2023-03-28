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




word = "hello"
print(dict_count(word))
