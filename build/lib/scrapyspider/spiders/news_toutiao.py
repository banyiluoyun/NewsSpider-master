# import requests
# from lxml import etree
# url = 'https://www.toutiao.com/ch/news_hot/'
# headers = {
# 'user-agent': 'Mozilla / 5.0(Windows NT 10.0; WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 53.0.2785.104Safari / 537.36Core / 1.53.4882.400QQBrowser / 9.7.13059.400'
# }
# cookies={'Cookie':'tt_webid=6767161080289625613; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6767161080289625613; csrftoken=7d774bfaa86e58c77103cb1ce5b711b4; sid_guard=3a770e843a873f5f410d7282667cd9e1%7C1575869925%7C5184000%7CFri%2C+07-Feb-2020+05%3A38%3A45+GMT; UM_distinctid=16eede1a72253c-0a3a1378a48b45-3b72025b-12b178-16eede1a723909; _ga=GA1.2.1263043391.1575949019; CNZZDATA1259612802=987444443-1575948890-%7C1577080775; s_v_web_id=k6u1tips_gAxqlzft_WN5z_4Qn0_BnGR_lMaEuaqArIYv; ttcid=40623259493046c896a707ca3f5ed55831; tt_scid=.dqh12TCEW74MjBX8QQh7gNRDDm0mg3Qs.rOqg-wjwxQyuN53DyZdLEu.DxnMjcm34c5; __tasessionId=54ycjy4591582261635606'}
# resp = requests.get(url=url,headers=headers,cookies=cookies)
# print(resp.text)
# content = resp.text.encode(resp.encoding).decode(resp.apparent_encoding)
# tree = etree.HTML(content)
# title_xpath = '//div[@class="title-box"]/a/@href'
# title = tree.xpath(title_xpath)
# print(title)