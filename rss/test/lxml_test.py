def read():
    import requests
    import lxml.html

    # WebサイトのURLを指定
    url = "https://status.aws.amazon.com/"

    # Requestsを利用してWebページを取得する
    r = requests.get(url)

    # lxmlを利用してWebページを解析する
    html = lxml.html.fromstring(r.text)

    # lxmlのfindallを利用して、ヘッドラインのタイトルを取得する
    elems = html.findall(".//td")

    for elem in elems:
        print(elem.text)

import time
start = time.time()
read()
print(time.time() - start)