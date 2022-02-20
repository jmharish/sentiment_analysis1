from nltk.tokenize import word_tokenize , sent_tokenize
from nltk.corpus import movie_reviews
from nltk import FreqDist
from nltk.classify import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import NuSVC
from nltk.classify import ClassifierI
from statistics import mode
import nltk
import pickle
import random
from nltk.tokenize import word_tokenize , sent_tokenize

class voting(ClassifierI):
    def __init__ (self , *classifiers):
        self.l = classifiers
    def voted_classify(self , features):
        votes = []
        for c in self.l:
            v = c.classify(features)
            votes .append(v)
        return mode(votes)
    def confidence (self , features):
        votes = []
        for c in self. l:
            v = c.classify(features)
            votes .append(v)
        choice = mode(votes)
        ctr = 0
        for c in votes:
            if(choice == c):
                ctr+=1
        return ctr/len(votes)
documents =[]
file3 = open("short_reviewes_negative.txt" , "r")
t = file3.read()
all_words = word_tokenize(t)
txt = sent_tokenize(t)
for c in txt:
        l=list(w.lower() for w in word_tokenize(c))
        documents.append((l,'neg'))
file3.close()
file3 = open("short_reviewes_positive.txt" , "r")
t = file3.read()
all_words+=word_tokenize(t)
txt = sent_tokenize(t)
for c in txt:
        l=list(w.lower() for w in word_tokenize(c))
        documents.append((l,'pos'))
file3.close()
all_words = FreqDist(all_words)
most_used = list(all_words.keys())[100:10100]

def find_features (doc):
    dooc = set(doc)
    features = {}
    for w in most_used :
        features[w] = (w in dooc)
    return features
feature_sets=[]

#for (words , cat) in documents:
#    feature_sets.append((find_features(words) ,cat))

feat_save = open('feat.pickle' , 'rb')
feature_sets = pickle.load(feat_save)
feat_save.close()



random.shuffle(feature_sets)
train_feat = feature_sets[:10000]
test_feat = feature_sets[10000:]

   # the trained and save(pickled) classifiers are loaded 
classifier_file = open ("sr2_naivebayes.pickle" , 'rb' )
classifier = pickle.load(classifier_file)
classifier_file.close()

classifier_save = open ("sr_MultinomialNB.pickle","rb")
MultinomialNB_classifier = pickle.load(classifier_save) 
classifier_save.close()

#classifier_save = open ("sr_NuSVC.pickle","rb")
#NuSVC_classifier = pickle.load(classifier_save)
#classifier_save.close()

classifier_save = open ("sr_LogisticRegression.pickle","rb")
LogisticRegression_classifier= pickle.load(classifier_save)
classifier_save.close()

def sentiment(text):
    feat = find_features(word_tokenize(text))
    voted_classifier = voting(MultinomialNB_classifier,classifier,LogisticRegression_classifier)# voted classifier containing different classifiers 
    t  = (voted_classifier.voted_classify(feat) , voted_classifier.confidence(feat))#classification is done, the class and the confidence is stored in tuple
    return t


