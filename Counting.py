def duplicate_count(text):
    upperText = text.upper()
    dict = {}
    result = 0
    
    for letter in upperText:
        if letter not in dict.keys():
            dict[letter] = 1
        else:
            dict[letter] += 1

    for count in dict.items():
        if count[1] >= 2:
            result += 1

    return result
    


print(duplicate_count("aabBcde"))