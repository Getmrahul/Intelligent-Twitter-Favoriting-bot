import twitter

CONSUMER_KEY = ""
CONSUMER_SECRET = ""
OAUTH_TOKEN = ""
OAUTH_TOKEN_SECRET = ""

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
twitter_api = twitter.Twitter(auth=auth)
print twitter_api

#Add hastag in the below array
hasharray = ['#tagsdock','#instagram','#hashtags','#vine']

count = 5
print hasharray

for k in hasharray:
	print k
	search_results = twitter_api.search.tweets(q=k, count=count)
	stat = search_results['statuses']
	for tweets in stat:
		try:
			print tweets['text'], '\n'
			result = twitter_api.favorites.create(_id=tweets['id'])
			print("favorited: %s" % (result['text'].encode("utf-8")))
		except twitter.api.TwitterHTTPError as e:
			print("error: %s" % (str(e)))

