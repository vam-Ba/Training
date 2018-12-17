import tweepy
from textblob import TextBlob
consumer_key = '1BZOlJxLP0kqxwOBmFJ3L8j98'
consumer_secret = 'nAFSSiQcKrOLxgKzOA7YmMEkABlQkLOdolSzjYKxCKSKOrKycv'
access_token = '902898911416696833-A3MQ9eKJLAT0VRzvPZvtBkndHl7YWV5'
access_token_secret ='m4msDrj9DzGX5EWOGEH62ynIOPNkFGQn9PiG7Q66aewhT'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
