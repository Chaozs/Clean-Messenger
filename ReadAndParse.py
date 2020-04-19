import timeit

#Test run time for splitting a string by spaces
setupSplitString = "msg = 'The small blue cow jumped over the high purple moon'"
splitString = "message = list(msg.split(' '))"
#Test execution 10000 times, and print average run time in milliseconds
print (timeit.timeit(setup = setupSplitString,
                    stmt = splitString,
                    number = 10000)/10)

#Test run time for caoncatenating a list of strings back into a string seperated by spaces
setupConcatenateList =  '''
filteredMsg = ""
words = ['The', 'small', 'blue', 'cow', 'jumped', 'over',
'the', 'high', 'blue', 'moon']
'''
caoncatenateList = '''
for word in words:
    filteredMsg = filteredMsg + word + " "
'''
#Test execution 10000 times, and print average run time in milliseconds
print (timeit.timeit(setup = setupConcatenateList,
                    stmt = caoncatenateList,
                    number = 10000)/10)

#Test run time for reading the file EnglishWords.txt
setupReadFileEnglishWords = "import WordChecker"
readFileEnglishWords = "englishWords = WordChecker.get_words_from_file('EnglishWords.txt')"
#Test execution 1000 times, and print average run time in milliseconds
print (timeit.timeit(setup = setupReadFileEnglishWords,
                    stmt = readFileEnglishWords,
                    number = 1000))

#Test run time for reading the file filter.txt
setupReadFileFilterList = "import WordChecker"
readFileFilterList = "englishWords = WordChecker.get_words_from_file('filter.txt')"
#Test execution 1000 times, and print average run time in milliseconds
print (timeit.timeit(setup = setupReadFileFilterList,
                    stmt = readFileFilterList,
                    number = 1000))
