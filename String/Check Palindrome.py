def check_palindrome(string):
    if string == string[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"

string = input("Enter a string: ")
print(check_palindrome(string))