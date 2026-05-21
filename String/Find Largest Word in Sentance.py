def largest_word(sentence):
    words = sentence.split()
    return max(words, key=len)


sentence = input("Enter a sentence: ")
print(largest_word(sentence))