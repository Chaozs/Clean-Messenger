# Test runtime for checking if a word exists, in list of EnglishWords
import timeit

#Load words from EnglishWords.txt into a list for setup
SETUP_CODE = '''
import Filter, WordChecker
englishWords = WordChecker.get_words_from_file("EnglishWords.txt")
'''

#Test time to check strings of length 1-6 exists in englishWords
existTest1char = "Filter.checkIfRealWord('c', englishWords)"
existTest2char = "Filter.checkIfRealWord('c', englishWords)"
existTest3char = "Filter.checkIfRealWord('c', englishWords)"
existTest4char = "Filter.checkIfRealWord('c', englishWords)"
existTest5char = "Filter.checkIfRealWord('c', englishWords)"
existTest6char = "Filter.checkIfRealWord('c', englishWords)"

#For each case, test 1000 executions, and print average runtime in millseconds
print (timeit.timeit(setup = SETUP_CODE, stmt = existTest1char, number = 1000))
print (timeit.timeit(setup = SETUP_CODE, stmt = existTest2char, number = 1000))
print (timeit.timeit(setup = SETUP_CODE, stmt = existTest3char, number = 1000))
print (timeit.timeit(setup = SETUP_CODE, stmt = existTest4char, number = 1000))
print (timeit.timeit(setup = SETUP_CODE, stmt = existTest5char, number = 1000))
print (timeit.timeit(setup = SETUP_CODE, stmt = existTest6char, number = 1000))
