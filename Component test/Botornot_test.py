import botometer

rapidapi_key = "3c54a6c8femshbc4b22db1abdd0cp17fffbjsnade7cdc09f41" # now it's called rapidapi key

twitter_app_auth = {
    'consumer_key': 'dYkKG6U7nF9eXcb7PCL1rmUj3',
    'consumer_secret': 'Vwi57HPdjo4euDVVk9RTXQYydJFdiEwzDSd1JQALPmQweXLyhq',
    'access_token': '2229645340-9Ktv9B0L2FQHm7v3pBWZTSDQcfnMqIXlSZmMCnD',
    'access_token_secret': 'D0DGLfTAT5yyqUzd2qqEbIDwYAmCBsLAAZZ2JC5fI8D2h',

  }

bom = botometer.Botometer(wait_on_ratelimit=True,
                          rapidapi_key=rapidapi_key,
                          **twitter_app_auth)

# Check a single account by screen name
result = bom.check_account('@clayadavis')

# Check a single account by id
result = bom.check_account(1548959833)

# Check a sequence of accountsj
# , '@onurvarol', '@jabawack'
accounts = ['@clayadavis']
for screen_name in bom.check_accounts_in(accounts):
    # Do stuff with `screen_name` and `result`
    print(result['display_scores'])
