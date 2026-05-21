def character_frequency(string):
    frequency = {}


    for ch in set(string):
        count = 0

        for letter in string:
            if letter == ch:
                count += 1

        frequency[ch] = count

    return frequency

string = input("Enter a string: ")
frequency = character_frequency(string)
