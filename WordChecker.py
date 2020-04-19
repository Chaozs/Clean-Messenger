
# Read file with english words, return list of all words seperated by newline
def get_words_from_file(filename):

    fileWords = open(filename, "r")
    words = fileWords.read().splitlines()
    fileWords.close()
    return words

# check if a string exists in a list of words that are passed in
def check_word_exists_in(words, stringToCheck):
    #Check if word exists in list of english words
    #check lowercase of filte word, as all strings in englishWords are lowercase
    return (stringToCheck.lower() in words)

def add_word_to_file(filename, stringToAdd):
    file = open(filename, "a+")
    file.write(stringToAdd)
    file.write("\n")
    file.close()

# remove a word from a file
def remove_string_from_file(filename, stringToCheck):
    filter = open(filename, "r+")
    filterWords = filter.readlines()
    filter.seek(0)
    for word in filterWords:
        if word.strip() != stringToCheck.strip():
            filter.write(word)
        else:
            pass
    filter.truncate()
    filter.close()
    return False
