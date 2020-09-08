def read():
    import requests
    import bs4
    import json
    import re

    # Web 情報取得
    url = 'https://status.aws.amazon.com/'
    get_url_info = requests.get(url)
    # BeautifulSoup オブジェクトを作成
    bs4Obj = bs4.BeautifulSoup(get_url_info.text, 'lxml')

    total_result = []

    for tr in bs4Obj.find('div',id='AP_block').find_all('tr'):
        for td in tr.find_all('td',class_="bb top pad8"):
            if re.search(r"Tokyo",td.text):
                tmp_result = {}
                tmp_result['servise'] = tr.find('td',class_="bb top pad8").text
                tmp_result['status'] = tr.find('td',class_="bb pad8").text
                tmp_result['rss'] = url + tr.find('a')['href']
                total_result.append(tmp_result)
    return total_result