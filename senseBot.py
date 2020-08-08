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

setup_Bot()

def godfred():
    name = "Godfred is a good boy"
    print(name)

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
        status = quote+" -"+author+"\n"+"#BBNaija♡ \
        #senseBot #dailyQuotes #Vote4LAycon #programming @godfredakpan"
        print('\nUpdating : ',status)
        api.update_status(status=status)
        print("\nGoing to Sleep for 1 min")
        time.sleep(60)
    except Exception as ex:
        print(ex)
        break