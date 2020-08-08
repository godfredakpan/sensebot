import requests
import tweepy
import time
import json
import credentials

consumerKey = credentials.consumerKey
consumerSecret = credentials.consumerSecret
accessToken = credentials.accessToken
accessTokenSecret = credentials.accessTokenSecret

class TwitterStreamListener(tweepy.streaming.StreamListener):
    ''' Handles data received from the stream. '''
    def on_status(self, status):
        print(status.id)
        print(status.user.name)
        print(status.text)
        return True

    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True # To continue listening

    def on_timeout(self):
        print('Timeout...')
        return True # To continue listening


listener = TwitterStreamListener()
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
stream = tweepy.streaming.Stream(auth, listener)
stream.filter(track=["#BBNaija"])