import word2vec

class Word2VecInterface:
    model = None

    #Load word2vec model stored in chat.bin in constructor
    def __init__(self):
        self.model = word2vec.load("Word2VecData/chat.bin")

    #Searches word2vec model for similar words, and return them
    def getWordsSimilarTo(self, word):
        try:
            indexes, metrics = self.model.similar(word)
            return self.model.vocab[indexes]
        except: #Return -1 indentifier if no words found
            return [-1]
