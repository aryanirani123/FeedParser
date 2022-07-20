#Get the structure of the website using FeedParser


import feedparser

NewsFeed = feedparser.parse("https://timesofindia.indiatimes.com/rssfeedstopstories.cms")

entry = NewsFeed.entries[0]

print(entry.keys())
