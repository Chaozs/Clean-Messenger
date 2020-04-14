import WordChecker, random
from Levenshtein import distance, hamming

#function for filtering a message. Will return a filtered message
def filterMessage(msg):
    #split message string into list of words, seperated by white space
    message = list(msg.split(" "))
    filterWords = WordChecker.get_words_from_file("filter.txt")
    englishWords = WordChecker.get_words_from_file("EnglishWords.txt")

    hammingDistance = 1
    levenshteinDistance = 2

    #for each word in list of words from message
    for index, word in enumerate(message):
        #check that current word is not a normal english word first
        if not checkIfRealWord(word, englishWords):
            #filter that word otherwise
            #message[index] = filterExact(message[index], generateRandomAsteriskString(), filterWords)
            #hamming distance of 1 can be inclusive of 0 for exact match also
            message[index] = filter(message[index], generateRandomAsteriskString(),
            filterWords, hammingDistance, levenshteinDistance)

    #rebuild the llist of words back into the message seperated by space
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

#unused
#function to filter exact matches to words on filter list
def filterExact(msg, asteriskString, filterWords):
    filteredMsg = msg
    for word in filterWords:
        #filteredMsg = filteredMsg.replace(word.strip(), asteriskString)
        pass
    return filteredMsg

#function to filter utilization hamming distance and Levenshtein distance
def filter(msg, asteriskString, filterWords, hammingDistance, levenshteinDistance):
    filteredMsg = msg
    #for each word in filter list
    for word in filterWords:
        #only check hamming distance of strings are same length
        if len(word.strip()) == len(msg.strip()):
            #if hamming distance isthe value passed in or less, censor it
            if hamming(word.strip(), msg.strip()) <= hammingDistance:
                filteredMsg = filteredMsg.replace(msg.strip(), asteriskString)
            #if not within hamming distance, check levenshtein distance is within range to be filtered
            elif distance(word.strip(), msg.strip()) <= levenshteinDistance:
                filteredMsg = filteredMsg.replace(msg.strip(), asteriskString)
        #if length not equal, check if within levenshtein distance length
        elif abs(len(word.strip()) - len(msg.strip()) <= levenshteinDistance):
            # check if levenshtein distance is within range to be filtered
            if distance(word.strip(), msg.strip()) <= levenshteinDistance:
                filteredMsg = filteredMsg.replace(msg.strip(), asteriskString)
    return filteredMsg

def checkIfRealWord(filterWord, englishWords):
    for word in englishWords:
        if filterWord.strip() == word.strip():
            return True
    return False
