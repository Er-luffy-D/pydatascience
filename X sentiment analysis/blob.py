# using textblob library 
# import nltk

# Ensure these two installed for proper working
# nltk.download('punkt_tab')
# nltk.download('averaged_perceptron_tagger_eng')
from textblob import TextBlob

wiki=TextBlob("Krishna is angry that he never gets good matches in Tinder")
print(wiki.tags)
print(wiki.words)

# checking the sentiment -1<sentiment<1
print(wiki.sentiment.polarity)

