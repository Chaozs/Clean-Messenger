import timeit

#Test execution times for hamming vs levenstein distance

#Import Levenshtein Library for setup
setup = "from Levenshtein import distance, hamming"

Hamming1 = "hamming('a', 'a')"
Levenshtein1 = "distance('a', 'a')"
#Test execution 10000 times, and print average run time in milliseconds
#print (timeit.timeit(setup = setup, stmt = Hamming1, number = 10000)/10)
print (timeit.timeit(setup = setup, stmt = Levenshtein1, number = 10000)/10)

Hamming2 = "hamming('be', 'be')"
Levenshtein2 = "distance('be', 'be')"
#Test execution 10000 times, and print average run time in milliseconds
#print (timeit.timeit(setup = setup, stmt = Hamming2, number = 10000)/10)
print (timeit.timeit(setup = setup, stmt = Levenshtein2, number = 10000)/10)

Hamming3 = "hamming('car', 'car')"
Levenshtein3 = "distance('car', 'car')"
#Test execution 10000 times, and print average run time in milliseconds
#print (timeit.timeit(setup = setup, stmt = Hamming3, number = 10000)/10)
print (timeit.timeit(setup = setup, stmt = Levenshtein3, number = 10000)/10)

Hamming4 = "hamming('hate', 'hate')"
Levenshtein4 = "distance('hate', 'hate')"
#Test execution 10000 times, and print average run time in milliseconds
#print (timeit.timeit(setup = setup, stmt = Hamming4, number = 10000)/10)
print (timeit.timeit(setup = setup, stmt = Levenshtein4, number = 10000)/10)

Hamming5 = "hamming('print', 'print')"
Levenshtein5 = "distance('print', 'print')"
#Test execution 10000 times, and print average run time in milliseconds
#print (timeit.timeit(setup = setup, stmt = Hamming5, number = 10000)/10)
print (timeit.timeit(setup = setup, stmt = Levenshtein5, number = 10000)/10)

Hamming6 = "hamming('random', 'random')"
Levenshtein6 = "distance('random', 'random')"
#Test execution 10000 times, and print average run time in milliseconds
#print (timeit.timeit(setup = setup, stmt = Hamming6, number = 10000)/10)
print (timeit.timeit(setup = setup, stmt = Levenshtein6, number = 10000)/10)
