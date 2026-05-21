def count_vowels_consonants(string):
    vowels = 0
    consonants = 0
    for ch in string.lower():
        if ch in 'aeiou':
            vowels += 1
        else:
            consonants += 1
    return vowels, consonants

string = input("Enter a string: ")
vowels, consonants = count_vowels_consonants(string)
print(vowels, consonants)