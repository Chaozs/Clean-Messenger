# Test runtime for checking if a word exists, in list of EnglishWords
import timeit

#Load words from EnglishWords.txt into a list for setup
SETUP_CODE = '''
import WordChecker
englishWords = WordChecker.get_words_from_file("EnglishWords.txt")
'''

#Test time to check strings of length 1-6 exists in englishWords
existTest1char = "WordChecker.check_word_exists_in(englishWords, 'c')"
existTest2char = "WordChecker.check_word_exists_in(englishWords, 'sd')"
existTest3char = "WordChecker.check_word_exists_in(englishWords, 'wef')"
existTest4char = "WordChecker.check_word_exists_in(englishWords, 'ewfk')"
existTest5char = "WordChecker.check_word_exists_in(englishWords, 'ergko')"
existTest6char = "WordChecker.check_word_exists_in(englishWords, 'oierfr')"

#For each case, test 1000 executions, and print average runtime in millseconds
print (timeit.timeit(setup = SETUP_CODE, stmt = existTest1char, number = 1000))
print (timeit.timeit(setup = SETUP_CODE, stmt = existTest2char, number = 1000))
print (timeit.timeit(setup = SETUP_CODE, stmt = existTest3char, number = 1000))
print (timeit.timeit(setup = SETUP_CODE, stmt = existTest4char, number = 1000))
print (timeit.timeit(setup = SETUP_CODE, stmt = existTest5char, number = 1000))
print (timeit.timeit(setup = SETUP_CODE, stmt = existTest6char, number = 1000))
