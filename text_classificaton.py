from nltk.tokenize import word_tokenize , sent_tokenize
from nltk.corpus import movie_reviews
from nltk import FreqDist
from nltk.classify import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB , GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import NuSVC
from nltk.classify import ClassifierI
from statistics import mode
import nltk
import pickle
import random 
'''

class voting(ClassifierI):
    def __init__ (self , *classifiers):
        self.l = classifiers # stores a list of classifier objects
    def voted_classify(self , features):
        votes = []
        for c in self.l:       #classification is done with different classifiers aginst the input feature
            v = c.classify(features)
            votes .append(v)
        return mode(votes) # returns the most common data (pos or neg) from  votes 
    def confidence (self , features):
        votes = []
        for c in self.l:
            v = c.classify(features)
            votes .append(v)
        choice = mode(votes) # the final choice (pos or neg) is the most common prediction among all the classifiers used
        ctr = 0
        for c in votes:
            if(choice == c):
                ctr+=1
        return ctr/len(votes) # returns the propotion of the final choice(pos or neg) among all the predictions




documents =[]
for c in movie_reviews.categories():    # neg and pos
    for f in movie_reviews.fileids(c):  
        l=list(movie_reviews.words(f))  #list of words in the review under the particular category(pos,neg)
        documents.append((l,c))         #stores the words in the review against the category as a tuple and appends in a list, holds all the reviews with category 
#print(len(documents))
all_words = movie_reviews.words()
all_words = FreqDist(all_words)         #sorts all the words in the set of reveiws from most to least frequent
most_used = list(all_words.keys())[100:3100] 
                                        #takes the most frequent 3000 words leaving out first 100 generic words which do not help in classification

def find_features (doc):
    dooc = set(doc)
    features = {}
    for w in most_used :
        features[w] = (w in dooc)
    return features

random.shuffle(documents) # shuffling the reviews 

feature_sets=[]
for (words , cat) in documents:
    feature_sets.append((find_features(words) ,cat))
#print(feature_sets[4])

train_feat = feature_sets[:1900]
test_feat = feature_sets[1900:]

#classifier = nltk.NaiveBayesClassifier.train(train_feat)
classifier_load =open('naivebayes.pickle' , 'rb')
classifier = pickle.load(classifier_load)
classifier_load.close()

#print ("classified" , classifier.classify(test_feat[0][0]),classifier.most_informative_features(10))
#classifier_save = open ("naivebayes.pickle" , 'wb' )
#pickle.dump(classifier , classifier_save)
#classifier_save.close()


##multinomialNB classifier ##
classifier_load =open("multinomialNB.pickle" , 'rb')
MultinomialNB_classifier = pickle.load(classifier_load)
classifier_load.close()
#print ("MNB accuracy" , nltk.classify.accuracy(MultinomialNB_classifier , test_feat))

##NuSVC classifier ##
classifier_load =open("NuSVC.pickle" , 'rb')
NuSVC_classifier = pickle.load(classifier_load)
classifier_load.close()
#print ("NuSVC accuracy" , nltk.classify.accuracy(NuSVC_classifier , test_feat)


##LogisticRegressionclassifier ##
#LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
#LogisticRegression_classifier.train(train_feat)
classifier_load =open("LogisticRegression.pickle", 'rb')
LogisticRegression_classifier = pickle.load(classifier_load)
classifier_load.close()
#print ("NuSVC accuracy" , nltk.classify.accuracy(LogisticRegression_classifier , test_feat)


voted_classifier = voting(MultinomialNB_classifier,classifier,NuSVC_classifier,LogisticRegression_classifier)
print( voted_classifier.confidence(test_feat[6][0]))


'''
feat_save = open('feat.pickle' , 'rb')
feature_sets = pickle.load(feat_save)
feat_save.close()

random.shuffle(feature_sets)
train_feat = feature_sets[:10000]
test_feat = feature_sets[10000:]


GaussianNB_classifier = SklearnClassifier(GaussianNB())
GaussianNB_classifier.train(train_feat)

classifier_save = open ('sr_GaussianNB.pickle' , 'wb')
pickle.dump(GaussianNB_classifier , classifier_save) #pickling is done here 1st parameter is the trained classifier (or object) 2nd parameter is the file opened in wb
classifier_save.close()                              # mode

print(GaussianNB_classifier.classify(test_feat[33][0]))















