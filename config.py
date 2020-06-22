import twitter
def getApi():
    return twitter.Api(consumer_key='key',
    consumer_secret='consumer_secret',
    access_token_key='access_token_key', #this will have to be generated when you make your app
    access_token_secret='access_token_secret') #this will have to be generated when you make your app