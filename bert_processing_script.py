import time

start = time.time()

from flair.embeddings import TransformerDocumentEmbeddings
from bertopic import BERTopic
import pandas as pd
import numpy as np
import matplotlib
import string
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer


sample_tweets = pd.read_csv("1_million_tweets.csv")                     ###  file_name must change
stripped_sample_tweets = sample_tweets[["created_at", "text"]]
stopwords = stopwords.words('english')
wordnet_lemmatizer = WordNetLemmatizer()
porter_stemmer = PorterStemmer()

def remove_punctuation(text):
    punctuationfree="".join([i for i in text if i not in string.punctuation])
    return punctuationfree

def tokenization(text):
    tokens = re.split(r'\W+', text)
    return tokens

#def remove_stopwords(text):
#    output= [i for i in text if i not in stopwords]
#    return output


stripped_sample_tweets['clean_text']= stripped_sample_tweets['text'].apply(lambda x:remove_punctuation(x))
stripped_sample_tweets['text_lower']= stripped_sample_tweets['clean_text'].apply(lambda x: x.lower())
stripped_sample_tweets['text_tokenied']= stripped_sample_tweets['text_lower'].apply(lambda x: tokenization(x))
#stripped_sample_tweets['no_stopwords']= stripped_sample_tweets['text_tokenied'].apply(lambda x:remove_stopwords(x))


##  The following code removes all html links from the tweets

tweets_list = []

for word_set in stripped_sample_tweets["text_tokenied"]:
    tweet_list = ""
    for text in word_set:
        if text[:4] != "http" and text[:3] != "www":
            tweet_list += text + " "
    tweets_list.append(tweet_list)


stripped_sample_tweets = stripped_sample_tweets[["created_at"]]
stripped_sample_tweets["preprocessed"] = tweets_list

## The following code moves the text into a list of strings for the BERTopic to fit into the topic model

tweet_list = []

for tweet in stripped_sample_tweets["preprocessed"]:
    tweet_list.append(tweet)

## The pre-trained embedding model we will use
covid_model = TransformerDocumentEmbeddings('digitalepidemiologylab/covid-twitter-bert-v2')
topic_model = BERTopic(embedding_model=covid_model)
topics, probs = topic_model.fit_transform(tweet_list)

topic_model.save("1_million_pretrained_model")

end = time.time()

print(end - start)