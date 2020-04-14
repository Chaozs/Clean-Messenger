import WordChecker
import random
import HammingDistance

#function for filtering a message. Will return a filtered message
def filterMessage(msg):
    #split message string into list of words, seperated by white space
    message = list(msg.split(" "))
    filterWords = WordChecker.get_words_from_file("filter.txt")
    englishWords = WordChecker.get_words_from_file("EnglishWords.txt")

    #for each word in list of words from message
    for index, word in enumerate(message):
        #check that current word is not a normal english word first
        if not checkIfRealWord(word, englishWords):
            #filter that word otherwise
            message[index] = filterExact(message[index], generateRandomAsteriskString(), filterWords)
            message[index] = filterHamming(message[index], generateRandomAsteriskString(), filterWords)

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

#function to filter exact matches to words on filter list
def filterExact(msg, asteriskString, filterWords):
    filteredMsg = msg
    for word in filterWords:
        filteredMsg = filteredMsg.replace(word.strip(), asteriskString)
    return filteredMsg

#function to replace all words with hamming distance of 1 from a word in filter list to be censored
def filterHamming(msg, asteriskString, filterWords):
    filteredMsg = msg
    #list of all common ASCII characters
    alphabet = "abcdefghijklmnopqrstuvwxyz01234567890[]{}';:,./<>?`~!@#$%^&*()-_=+`"
    #for each word in filter list
    for word in filterWords:
        #for each possible string within hamming distance 1
        for item in HammingDistance.hamming_circle(word.strip(), 1, alphabet):
            filteredMsg = filteredMsg.replace(item.strip(), asteriskString)
    return filteredMsg

def checkIfRealWord(filterWord, englishWords):
    for word in englishWords:
        if filterWord.strip() == word.strip():
            return True
    return False
