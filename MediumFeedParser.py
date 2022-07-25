import feedparser
from numpy import number

feed_url = "https://aryanirani123.medium.com/feed"

blog_feed = feedparser.parse(feed_url)

#Gets the title of the website
#website_title = blog_feed.feed.title
#print(website_title)

#get the list of blogs in the article
#blogs = blog_feed
#print(blogs)

content = blog_feed.entries
#print(content)


#print(len(blog_feed.entries))
#numberofblogs = len(blog_feed.entries)
#print(numberofblogs)

for blog in content:

    print(blog.title)
    print(blog.link)
    print(blog.published)
