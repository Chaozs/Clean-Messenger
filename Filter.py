import WordChecker
import random

#function for filtering a message. Will return a filtered message
def filterMessage(msg):
    filterWords = WordChecker.get_words_from_file("filter.txt")
    numAsterisks = random.randrange(2,6)
    asteriskString = ""
    englishWords = WordChecker.get_words_from_file("EnglishWords.csv")

    for i in range(numAsterisks):
        asteriskString = asteriskString + "*"
    filteredMsg = filterExact(msg, asteriskString, filterWords)
    return filteredMsg

#function to filter exact matches to words on filter list
def filterExact(msg, asteriskString, filterWords):
    for word in filterWords:
        filteredMsg = msg.replace(word.strip(), asteriskString)
    return filteredMsg
