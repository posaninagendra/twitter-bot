#!/usr/bin/env python

import tweepy

# from our keys module (keys.py), import the keys dictionary
from keys import keys

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

query = " "

tweet_lists = api.search(q=query, count=20, lang="en")

for tweet in tweet_lists:
	screenname = tweet.user.screen_name
	message = ".@{username} {message}".format(username=screenname, message=' ')
	try:
		api.update_status(status=message, in_reply_to_status_id=tweet.id)
		print message
	except tweepy.TweepError as e:
		print e.message[0]['code']
		print e.args[0][0]['code']

