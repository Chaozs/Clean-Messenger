
# Read file with english words, return list of all words seperated by newline
def init_word_database() :

    fileWords = open('EnglishWords.csv', 'r')
    englishWords = fileWords.readlines()
    filter.close()
    return englishWords

# check if a string exists in a list of words
def check_word_exists_in(englishWords, stringToCheck) :
    for word in englishWords:
        #print (word.strip())
        if word.strip() == stringToCheck:
            return True
    return False

# Check if a string exists in specified file
def check_if_in_file(filename, stringToCheck) :
    exists = False
    file = filename + ".txt"
    print(file)
    filter = open(file, "r")
    filterWords = filter.readlines()
    for word in filterWords:
        if word.strip() == stringToCheck.strip():
            filter.close()
            return True
    filter.close()
    return False
