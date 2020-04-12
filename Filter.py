import WordChecker
import random
import HammingDistance

#function for filtering a message. Will return a filtered message
def filterMessage(msg):
    filterWords = WordChecker.get_words_from_file("filter.txt")
    numAsterisks = random.randrange(2,6)
    asteriskString = ""
    englishWords = WordChecker.get_words_from_file("EnglishWords.csv")

    for i in range(numAsterisks):
        asteriskString = asteriskString + "*"
    filteredMsg = filterExact(msg, asteriskString, filterWords)
    filteredMsg = filterHamming(filteredMsg, asteriskString, filterWords, englishWords)
    return filteredMsg

#function to filter exact matches to words on filter list
def filterExact(msg, asteriskString, filterWords):
    filteredMsg = msg
    for word in filterWords:
        filteredMsg = filteredMsg.replace(word.strip(), asteriskString)
    return filteredMsg

#function to replace all words with hamming distance of 1 from a word in filter list to be censored
def filterHamming(msg, asteriskString, filterWords, englishWords):
    filteredMsg = msg
    #list of all common ASCII characters
    alphabet = "abcdefghijklmnopqrstuvwxyz01234567890[]{}';:,./<>?`~!@#$%^&*()-_=+`"
    #for each word in filter list
    for word in filterWords:
        #for each possible string within hamming distance 1
        for item in HammingDistance.hamming_circle(word.strip(), 1, alphabet):
            if checkIfRealWord(item, englishWords) == False:
                filteredMsg = filteredMsg.replace(item.strip(), asteriskString)
    return filteredMsg

def checkIfRealWord(filterWord, englishWords):
    for word in englishWords:
        if filterWord == word:
            return True
    return False
