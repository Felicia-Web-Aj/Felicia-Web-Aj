print ("Hello from app.py!")
from textblob import TextBlob
print("welcome to the Sentiment Analyzer")
sentence = input("Enter a sentence to analyze:")
blob = TextBlob(sentence)
Sentiment = blob.sentiment.polarity
if Sentiment>0:
   print("Sentiment:Positive😊")
elif Sentiment<0:
   print("Sentiment:Negative😞")
else:
   print("Sentiment:Neutral😐")
