
# Read file with english words, return list of all words seperated by newline
def init_word_database() :

    fileWords = open('EnglishWords.csv', 'r')
    englishWords = fileWords.readlines()
    return englishWords

# check if stringToCheck exists in list of englishWords
def check_word_exists(englishWords, stringToCheck) :
    for word in englishWords:
        #print (word.strip())
        if word.strip() == stringToCheck:
            return True
    return False
    
#testing
englishWords = init_word_database()
print (check_word_exists(englishWords, "test"))
print (check_word_exists(englishWords, "hello"))
print (check_word_exists(englishWords, "alone"))
print (check_word_exists(englishWords, "alose4gerne"))
