import settings
import requests
import tweepy
import os
import sys
reload(sys)
sys.setdefaultencoding('ISO-8859-1')

def twitter_api():
    consumer_key = settings.TWITTER_CONSUMER_KEY
    consumer_secret = settings.TWITTER_CONSUMER_SECRET
    access_token = settings.TWITTER_ACCESS_TOKEN
    access_token_secret = settings.TWITTER_ACCESS_SECRET

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api

def tweet_image(url, message):
    api = twitter_api()
    filename = 'temp.gif'
    request = requests.get(url, stream=True)
    print url
    if request.status_code == 200:
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)

        api.update_with_media(filename, status=message)
        os.remove(filename)
    else:
        print("Unable to download image")

with open('gifs.txt', 'r') as fin:
    data = fin.read().splitlines(True)
with open('gifs.txt', 'w') as fout:
    fout.writelines(data[1:])
with open('tweeted.txt', 'a') as f:
    f.writelines(data[0])

url = data[0].rstrip('\n')
message = data[0].rstrip('\n')
tweet_image(url, message)