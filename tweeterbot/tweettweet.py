import tweepy
import time

auth = tweepy.OAuthHandler('MopVS9lf0oyANk54ITDf6FCXN', 'fq9O4hN1XehsntyedatkCvQA3BQhhARUUbW8BDgNmoSYAUSwmp')
auth.set_access_token('2292306206-0dLm49XxSZofn6sDqpmAa5WPXBzauyj2GteMuSk', 'XHFFZVYTSVVef6Ax9qTge1ocW8dXbcSsqQl3zGZpiAuP1')

api = tweepy.API(auth)

user = api.me()
print (user.name) #prints your name.
print (user.screen_name)
print (user.followers_count)

search = "#T20WorldCup"
numberOfTweets = 2

def limit_handle(cursor):
  while True:
    try:
      yield cursor.next()
    except tweepy.RateLimitError:
      time.sleep(1000)

#Be nice to your followers. Follow everyone!
# for follower in limit_handle(tweepy.Cursor(api.followers).items()):
#   #if follower.name == 'Usernamehere':
#     print(follower.name)
#     follower.follow()


# Be a narcisist and love your own tweets. or retweet anything with a keyword!
for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        tweet.favorite()
        print('Retweeted the tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break