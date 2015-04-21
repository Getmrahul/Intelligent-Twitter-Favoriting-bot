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
#statuses = twitter_api.statuses.user_timeline(screen_name = '@xyz', max_count= 30, include_entities=1 )
#for tweet in statuses:
#	try:
#		for hashtag in tweet['entities']['hashtags']:
#			print hashtag['text']
#			hashtagtext = '#' +hashtag['text'] 
#			hasharray.append(hashtagtext)
#	except twitter.api.TwitterHTTPError as e:
#		print("error: %s" % (str(e)))
count = 5
print hasharray
#newarray = []

#for i in hasharray:
#	if i not in newarray:
#		newarray.append(i)
#print newarray

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

