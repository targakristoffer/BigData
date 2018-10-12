import nltk
from nltk.tokenize import PunktSentenceTokenizer
from nltk.chunk import *
from sklearn import svm
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

import re

###
##
#
class Basic_NLP_Tasks():
    def __init__(self):
        super().__init__()
        self.stop_words = set(stopwords.words("English"))
        self.PortStemmer = PorterStemmer()
        self.eng_vocab = set(w.lower() for w in nltk.corpus.words.words())

    def return_tasks(self):
        print("[+] All tasks in basic tasks")

    def remove_stopwords(self, sentence):
        sentence_filtered = []
        sentence_filtered = [w for w in sentence if not w in self.stop_words]
        return sentence_filtered

    def stem_words(self, words):
        for word in words:
            print('---------------> ', word)

        words = [self.PortStemmer.stem(word) for word in words if not word.isdigit()]

        for word in words:
            print('++++++++++++++++> ', word)
        
        return words

    ## For finding other words
    def findTags(self, tagList):
        arr = []
        testarr = []
        for word, tag in tagList:
            tag = str(tag).strip().upper()
            if(tag == 'NNS' or tag == 'NN' or tag == 'VB' or tag == 'NNP'):
                testarr.append(tag)
                arr.append(word)
        
        return arr

    def isEnglishWord(self, words):
        words = [word for word in words if word in self.eng_vocab]
        return words


class POS_Retriever(Basic_NLP_Tasks):
    def __init__(self):
        super().__init__()

    def find_POS(self, content):
        print('(-) 1')
        print("[+] NER CLASS IS UP")
        print(content)
        print('(-) 2')
        arrResult = self.getPOS(content)

        return arrResult

        

    def getPOS(self, content):
        
        arrOfResult = []
        seperator = "'\n'------------------------------SENTENCE--------------------------------"
        get_custom_tok = PunktSentenceTokenizer(content)
        tokens = get_custom_tok.tokenize(content)
        try: 
            for i in tokens:
                tagged = nltk.pos_tag(nltk.word_tokenize(i), lang='eng')
                text = ''.join(str(tagged))
               
                arrOfResult.append(text)
                arrOfResult.append(seperator)
            return arrOfResult

        except Exception as e:
            print(str(e))
           


class NER_Retriever(Basic_NLP_Tasks):
    def __init__(self):
        super().__init__()
    
    def find_NER(self, content):
        print('(+) FINDING NERs - 1')
        arrResults = self.getNER(content)
    
        return arrResults

    def getNER(self, content):
        get_custom_tok = PunktSentenceTokenizer(content)
        tokens = get_custom_tok.tokenize(content)
        seperator = "'\n'------------------------------SENTENCE--------------------------------"
        arrOfResult = {}
        print('(+) FINDING NERs - 2')
        try: 
            for i in tokens:
                text = ''
                words = nltk.word_tokenize(i)
                tagged = nltk.pos_tag(nltk.word_tokenize(i))
                namedEnt = nltk.ne_chunk(tagged, binary=True)
                print('(+) FINDING NERs - 3')
                arrOfResult = self.cleanEntityList(arrOfResult, words, namedEnt)
                print('(+) FINDING NERs - 4')
            return arrOfResult

        except Exception as e:
            print(str(e))

    def cleanEntityList(self, arr, sentence, ent):
        print('(+) FINDING NERs - 3.5')
        arr[str(sentence)] = []
        print('(+) FINDING NERs - 3.6')
        print('(+) FINDING NERs - 3.7')
        for chunk in ent:
            if hasattr(chunk, 'label'):
                print(chunk.label(), ' '.join(c[0] for c in chunk))
                arr[str(sentence)].append(str((chunk.label(), ' '.join(c[0] for c in chunk))))

        return arr