from twitter import *

# This class handles interactions with twitter
class twitter:
	def __init__(self):
		# Load API credentials
		config = {}
		execfile("twitter_config.py", config)

		self.twitter = Twitter(
			auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))

	# Returns a list of current trends
	def get_trends(self):
		# Retrieve London trends (Hard coded)
		results = self.twitter.trends.place(_id = 44418)

		trends = []
		for location in results:
			for trend in location["trends"]:
				trends.append(trend["name"])
		return trends

	# Returns a list of tweets based on a keyword / trend
	def get_tweets(self, trend):
		tweets = []
		query = self.twitter.search.tweets(q = trend, geocode = "51.494976,-0.122232,30km",count="100",lang="en")

		for result in query["statuses"]:
			tweets.append(result["text"])
		return tweets
