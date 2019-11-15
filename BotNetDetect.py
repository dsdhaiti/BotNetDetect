import tweepy
import time

def get_tw_auth(key):
    twitter_app_auth = {
        'consumer_key': 'dYkKG6U7nF9eXcb7PCL1rmUj3',
        'consumer_secret': 'Vwi57HPdjo4euDVVk9RTXQYydJFdiEwzDSd1JQALPmQweXLyhq',
        'access_token': '2229645340-9Ktv9B0L2FQHm7v3pBWZTSDQcfnMqIXlSZmMCnD',
        'access_token_secret': 'D0DGLfTAT5yyqUzd2qqEbIDwYAmCBsLAAZZ2JC5fI8D2h',

    }
    return twitter_app_auth[key]
def auth_tweepy():
    auth = tweepy.OAuthHandler(get_tw_auth('consumer_key'), get_tw_auth('consumer_secret'))
    auth.set_access_token(get_tw_auth('access_token'), get_tw_auth('access_token_secret'))
    tweepyapi = tweepy.API(auth)
    return tweepyapi

if __name__ == '__main__':
    user = '@dannydeacon1970'

    # get handle from the user
    print("please enter you starting users handle")

    print("Is the handle user:",user +"\n")

    #initilize  and set the starting users
    api_tweepy = auth_tweepy()
    user_tw =  api_tweepy.get_user(user)

    # # number of follwoers
    # user_followerCount = user_tw.followers_count
    # print('Number of followers: ',user_tw.followers('screen_name'))

    # list followers
    # count = 0
    # for user in api_tweepy.followers(user):
    #     print(str(user.screen_name)+ '\n')
    #     count += 1
    # print(count)

    ids = []
    for page in tweepy.Cursor(api_tweepy.followers_ids, screen_name=user).pages():
        ids.extend(page)
        time.sleep(60)

    print
    len(ids)

    # begin the process
    #     check all the followers to see if they are bots
    #     output the bots in a list
    #      todo: implement diagraming the netowrk
