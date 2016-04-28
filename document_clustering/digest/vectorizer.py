import pandas as pd
from document_clustering.digest.tokenizer import tokenize_and_stem
from document_clustering.digest.tokenizer import tokenize_only
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class Vectorizer:
    tfidf_vectorizer = None
    vocab_frame = None
    tfidf_matrix = None
    terms = None
    dist = None

    def __init__(self):
        #define vectorizer parameters # max = 0.8 min = 0.2
        self.tfidf_vectorizer = TfidfVectorizer(
            max_df=0.5, max_features=200000,
            min_df=2, stop_words='english',
            use_idf=True, tokenizer=tokenize_and_stem, ngram_range=(1,3))

    def vectorize(self, descriptions):
        total_vocab_stemmed = []
        total_vocab_tokenized = []
        for text in descriptions:
            allwords_stemmed = tokenize_and_stem(text) #for each item in 'synopses', tokenize/stem
            total_vocab_stemmed.extend(allwords_stemmed) #extend the 'totalvocab_stemmed' list

            allwords_tokenized = tokenize_only(text)
            total_vocab_tokenized.extend(allwords_tokenized)

        self.vocab_frame = pd.DataFrame({'words': total_vocab_tokenized}, index=total_vocab_stemmed)
        self.tfidf_matrix = self.tfidf_vectorizer.fit_transform(descriptions) #fit the vectorizer to synopses
        self.terms = self.tfidf_vectorizer.get_feature_names()
        self.dist = 1 - cosine_similarity(self.tfidf_matrix)

    def vocab_frame_(self):
        # print 'There are ' + str(self.vocab_frame.shape[0]) + ' items in vocab_frame'
        return self.vocab_frame

    def tfidf_matrix_(self):
        # print 'The TF-IDF matrix has a dimension of: %s' % str(self.tfidf_matrix.shape)
        return self.tfidf_matrix

    def terms_(self):
        return self.terms

    def dist_(self):
        return self.dist
