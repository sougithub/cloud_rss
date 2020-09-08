
def read():
    import feedparser
    RSS_URL = "https://status.cloud.google.com/feed.atom"

    gcp_rss = feedparser.parse(RSS_URL)

    rss_array = []
    response = {}
    response['lastupdate'] = gcp_rss.updated

    for entry in gcp_rss.entries:
        # print(entry)
        rss = {}
        rss['title'] = entry.title
        rss['link']  = entry.link
        rss['updated']  = entry.updated
        rss_array.append(rss)
        
    response['rss'] = rss_array
    return response
# print(read())