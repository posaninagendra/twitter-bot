# A simple twitter bot
This bot helps you to reply with custom messages to particular topic by searching its tweets in twitter. 
### How it works?:
1. Access Twitter APIs
2. Search for tweets with a query
3. Reply to the tweets of the query with a custom message. 

### Dependency
1. tweepy python library
2. Create a twitter app and generate access keys to the app

### How to use it?
1. Create a twitter account if doesn't exit
2. Create a twitter app at [apps@twitter](apps.twitter.com)
3. Generate access tokens for the app and use these tokens with customer tokens to fill the keys dictionary in keys.py
4. Modify bot.py by changing the query stirng to search for a particular topic
5. Modify the custome message to write your message
6. Run: $python bot.py
7. Open your twitter account, enjoy the fun!
