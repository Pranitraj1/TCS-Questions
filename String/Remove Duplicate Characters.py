def remove_duplicate_chars(s):
    result = ""

    for ch in s:
        if ch in result:
            result += ch

    return result

string = input("Enter a string: ")
print(remove_duplicate_chars(string))