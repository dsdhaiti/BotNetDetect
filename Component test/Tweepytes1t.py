import tweepy
import time
consumer_key = "dYkKG6U7nF9eXcb7PCL1rmUj3"
consumer_secret = "Vwi57HPdjo4euDVVk9RTXQYydJFdiEwzDSd1JQALPmQweXLyhq"

access_token = "2229645340-9Ktv9B0L2FQHm7v3pBWZTSDQcfnMqIXlSZmMCnD"
access_token_secret = "D0DGLfTAT5yyqUzd2qqEbIDwYAmCBsLAAZZ2JC5fI8D2h"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user = api.get_user('@clayadavis')

# api.followers
# public_tweets = api.home_timeline()

# for tweet in public_tweets:
#     print(tweet.text)

def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(15 * 60)

for follower in limit_handled(tweepy.Cursor(api.followers).items()):
    if follower.friends_count < 300:
        print(follower.screen_name)