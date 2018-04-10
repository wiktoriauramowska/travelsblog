import tweepy

auth = tweepy.OAuthHandler("0SKohKeusYV36sM7bKgLil0LZ","6aoAyxWbEhGjCrpv1EWSBEtXK5I10lsdiJAJlXm9lvf7E1v4XL")
auth.set_access_token ("701267940885340161-mt2uIgz9vMPSFAzRtAkQjeZIqOp54er", "dkznlFrYZkIZyf0HI0X60xEXMaicnR2O1XwoWksJoLejO")

twitter_api = tweepy.API(auth)

travel_tweets = twitter_api.search(
	#Twitter handles what you want to search by
	q = "Travel",
	r = "World", 
	s = "Traveling",
	t = "traveler",
	u = "worldwonder",
	v = "wanderlust",
	w = "ilovetravel",
	y = "trip",
	z = "holiday"
)

for tweet in travel_tweets:
	print tweet.user.name + ": " + tweet.text +"\n"

