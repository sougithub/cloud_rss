
def read():
    import feedparser
    RSS_URL = "https://azurestatuscdn.azureedge.net/ja-jp/status/feed/"

    azure_rss = feedparser.parse(RSS_URL)

    rss_array = []
    response = {}
    response['tile'] = azure_rss.feed.title
    response['lastupdate'] = azure_rss.updated

    for entry in azure_rss.entries:
        rss = {}
        rss['title'] = entry.title
        rss['link']  = entry.link
        rss['pubDate']  = entry.published
        rss_array.append(rss)
    response['rss'] = rss_array
    print(response)
