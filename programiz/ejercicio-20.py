# Write a function to censor words that are longer than four characters in a sentence
def censor_words(sentence):
    words = sentence.split()
    censored = []
    for word in words:
        if len(word) > 4:
            censored.append('*' * len(word))
        else:
            censored.append(word)
    return " ".join(censored)

# Example usage
input_sentence = "This function will censor words that are longer than four characters"
print(censor_words(input_sentence))
