import matplotlib.pyplot as plt
import networkx as nx
import twint as tw
import botometer
def config_twitter():
    twitter_app_auth = {
        'consumer_key': 'dYkKG6U7nF9eXcb7PCL1rmUj3',
        'consumer_secret': 'Vwi57HPdjo4euDVVk9RTXQYydJFdiEwzDSd1JQALPmQweXLyhq',
        'access_token': '2229645340-9Ktv9B0L2FQHm7v3pBWZTSDQcfnMqIXlSZmMCnD',
        'access_token_secret': 'D0DGLfTAT5yyqUzd2qqEbIDwYAmCBsLAAZZ2JC5fI8D2h',

    }
    return twitter_app_auth

def check_user(usernmae):
    rapidapi_key = "3c54a6c8femshbc4b22db1abdd0cp17fffbjsnade7cdc09f41"
    twitter_app_auth = config_twitter()
    bom = botometer.Botometer(wait_on_ratelimit=True,
                              rapidapi_key=rapidapi_key,
                              **twitter_app_auth)

    # Check a single account by screen name
    result = bom.check_account('@' + usernmae)

    #check theshold of 3.5
    if (result['display_scores']['english'] > 3.5):
        return True



def get_following(username):
    c = tw.Config()

    c.Username = username
    # number of searchs that i will be doing
    c.Limit = 20
    c.Store_object = True
    c.Hide_output = True
    tw.run.Followers(c)
    followers = tw.output.follows_list
    return followers

def networkCreator(username,degree,G):

    #base case
    if degree == 0:
        return G

    # get list of following
    following = get_following(username)
    if len(following) <1:
        return "failed test"

    # create list of bots
    bots = []

    # loop through following 
     for x in following:
         #check if bot
         if check_user(x):
    
             #append to bots list
             bots.append(x)

    # loop through  list of bots
    for x in bots:
        #create node
        G.add_node(x)

        # add edge from the name to the
        G.add_edge(username,x)

        #recursive run through
        degree-=1
        networkCreator(x,degree,G)

if __name__ == '__main__':
    username = "shallowtay"
    degree = 2

    G = nx.Graph()
    G.clear()
    G.add_node(username)

    networkCreator(username,degree,G)

    nx.draw(G,with_labels = True)
    plt.savefig("path_graph1.png")
    plt.show()
