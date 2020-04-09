import word2vec

class Word2VecInterface:
    model = None

    def __init__(self):
        print("init")
        self.model = word2vec.load("Word2VecData/chat.bin")

    def getWordsSimilarTo(self, word):
        try:
            indexes, metrics = self.model.similar(word)
            return self.model.vocab[indexes]
        except:
            return [-1]
