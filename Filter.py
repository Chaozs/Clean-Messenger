import WordChecker, random
from Levenshtein import distance, hamming

#function for filtering a message. Will return a filtered message
def filterMessage(msg, levenshteinDistance):
    #split message string into list of words, seperated by white space
    message = list(msg.split(" "))
    filterWords = WordChecker.get_words_from_file("filter.txt")
    englishWords = WordChecker.get_words_from_file("EnglishWords.txt")

    #for each word in list of words from message
    for index, word in enumerate(message):
        #Skip empty strings
        if len(word) == 0:
            pass
        else:
            message[index] = filterLevenshtein(message[index], filterWords,
            englishWords, levenshteinDistance)
    #rebuild the list of words back into the message seperated by space
    filteredMsg = ""
    for word in message:
        filteredMsg = filteredMsg + word + " "
    return filteredMsg

#generate a string consisting of random number of asterisks 2-5 in length
def generateRandomAsteriskString():
    numAsterisks = random.randrange(2,6)
    asteriskString = ""
    for i in range(numAsterisks):
        asteriskString = asteriskString + "*"
    return asteriskString

#unused - testing purposes only
#function to filter exact matches to words on filter list
def filterExact(msg):
    filteredMsg = msg
    filterWords = WordChecker.get_words_from_file("filter.txt")
    for word in filterWords:
        filteredMsg = filteredMsg.replace(word, generateRandomAsteriskString())
    return filteredMsg

#function to filter utilization hamming distance and Levenshtein distance
def filter(msg, filterWords, englishWords, hammingDistance, levenshteinDistance):
    #Filter special characters from string
    filteredMsg = ''.join(e for e in msg if e.isalnum())
    #for each word in filter list
    for word in filterWords:
        #for all criteria check if it's a proper english word before filtering it
        #If a word matches a filter criteria, and is not an english word, the asterisk string is returned
        #only check hamming distance of strings are same length
        if len(word) == len(filteredMsg):
            #if hamming distance isthe value passed in or less, censor it
            if hamming(word, filteredMsg) <= hammingDistance:
                if not WordChecker.check_word_exists_in(englishWords, filteredMsg):
                    return generateRandomAsteriskString()
            #if not within hamming distance, check levenshtein distance is within range to be filtered
            elif distance(word, filteredMsg) <= levenshteinDistance:
                if not WordChecker.check_word_exists_in(englishWords, filteredMsg):
                    return generateRandomAsteriskString()
        #if not same length, check if within levenshtein distance insert range
        elif abs(len(word) - len(filteredMsg) <= levenshteinDistance):
            if distance(word, filteredMsg) <= levenshteinDistance:
                if not WordChecker.check_word_exists_in(englishWords, filteredMsg):
                    return generateRandomAsteriskString()
    # Otherwise, return original string
    return msg


#function to filter utilizating Levenshtein distance
def filterLevenshtein(msg, filterWords, englishWords, levenshteinDistance):
    #Filter special characters from string
    filteredMsg = ''.join(e for e in msg if e.isalnum())
    #for each word in filter list
    for word in filterWords:
        #for all criteria check if it's a proper english word before filtering it
        #If a word matches a filter criteria, and is not an english word, the asterisk string is returned
        if abs(len(word) - len(filteredMsg) <= levenshteinDistance):
            if distance(word, filteredMsg) <= levenshteinDistance:
                if not WordChecker.check_word_exists_in(englishWords, filteredMsg):
                    return generateRandomAsteriskString()
    # Otherwise, return original string
    return msg
