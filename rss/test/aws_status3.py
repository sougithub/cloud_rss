from html.parser import HTMLParser
import urllib.request
import re

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.deeper = 0
        self.tmp = {}
        self.total = []

    def handle_starttag(self, tag, attrs):
        # AP_Block配下でのみカウントアップする
        if self.deeper > 0:
            self.deeper = self.deeper + 1

        for attr in attrs:
            if('AP_block' in attr):
                self.deeper = self.deeper + 1
                if self.deeper >= 5:
                    print("ID:",attr)
                    print("deeper:",self.deeper)
            else:
                if self.deeper >= 5:
                    print("attr",attr)

    def handle_endtag(self, tag):
        if self.deeper > 0:
            self.deeper = self.deeper - 1
            if self.deeper >= 5:
                print("Encountered an end tag :", tag)
                print("deeper:",self.deeper)

    def handle_data(self, data):
        if self.deeper >= 5:
            if len(data) > 0:
                str = ''.join(data)
                str = re.sub(r'\s','',str)
                if str:
                    print("Encountered some data  :", str)

def aws_status():
    import ssl
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    f = urllib.request.urlopen('https://status.aws.amazon.com/',context=context)

    parser = MyHTMLParser()
    parser.feed(f.read().decode())

import time
start = time.time()
aws_status()
print(time.time() - start)