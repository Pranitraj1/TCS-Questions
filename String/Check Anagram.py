def check_anagram(string1, string2):
    if sorted(string1) == sorted(string2):
        return ("Anaagaram")
    else:
        return ("Not Anagram")

string1 = input("Enter a string: ")
string2 = input("Enter another string: ")
print(check_anagram(string1, string2))