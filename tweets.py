import tweepy
from textblob import TextBlob

consumer_key = 'Your Customer key'
consumer_secret = 'Your secret '

access_token = 'your access token'
access_token_secret = 'Your access token secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweet = api.search('trump')

for tweet in public_tweet:
  print(tweet.text)


  analysis = TextBlob(tweet.text)
  if analysis.sentiment.polarity > 0:
      print('positive')
  elif analysis.sentiment.polarity ==0:
      print('neutral')
  else:
      print('Negative')

if analysis.sentiment.subjectivity ==0:
    print('80-100 percent factual')
elif analysis.sentiment.subjectivity >= 0.5:
    print('50 to 80 percent factual')
else:
    print('most likely an opinion')

print(analysis.sentiment)
print("")
