import requests
import tweepy
import time
import json
import credentials

def setup_Bot():
    consumerKey = credentials.consumerKey
    consumerSecret = credentials.consumerSecret
    accessToken = credentials.accessToken
    accessTokenSecret = credentials.accessTokenSecret
    auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
    auth.set_access_token(accessToken, accessTokenSecret)
    api = tweepy.API(auth)
    return api

def godfred():
    description = "Creator of SenseBot"
    print(description)

def get_Quote():
    params = {
        'method':'getQuote',
        'lang':'en',
        'format':'json'
    }

    res = requests.get('http://api.forismatic.com/api/1.0/',params)
    jsonText =json.loads(res.text)
    return jsonText["quoteText"],jsonText["quoteAuthor"]

api = setup_Bot()
while True:
    try:
        quote,author = get_Quote()
        status = quote+" -"+author+"\n"+"\
        #inspiration #motivation"
        print('\nUpdating : ',status)
        api.update_status(status=status)
        print("\nGoing to Sleep for 1  hour")
        time.sleep(3600)
    except Exception as ex:
        print(ex)
        break