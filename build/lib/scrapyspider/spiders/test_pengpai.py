import requests
# from lxml import etree
#
# # url = "https://www.thepaper.cn/load_chosen.jsp?nodeids=25949&topCids=6043251,6043255,6043151,6042428,6043144,&pageidx=5&lastTime=1582070444798"
# # url2 = 'https://www.thepaper.cn/newsDetail_forward_6040960'
# # url3 = 'https://www.thepaper.cn/load_index.jsp?nodeids=90069,&channelID=90077&topCids=,6043229,6043155,6042441,6043227,6042335&pageidx=2&lastTime=1582075279003'
# # url4 = 'https://www.thepaper.cn/load_index.jsp?nodeids=90069,&channelID=90077&topCids=,6043229,6043155,6042441,6043227,6042335&pageidx=25'
# # url5 = 'https://www.thepaper.cn/channel_25950'
# # url6 = 'https://www.thepaper.cn/newsDetail_forward_6045198'
#
# url = 'https://www.thepaper.cn/newsDetail_forward_6067051'
# url = 'https://世界末流大学.com'
# resp = requests.get(url)
# print(resp.status_code)
# print(resp.text)
# content = resp.text.encode(resp.encoding).decode(resp.apparent_encoding)
# tree = etree.HTML(content)
# # path_link = '//*[@id="listContent"]/div/h2/a/@href'
# # xpath_detail4 = '//div[@class="news_txt"]'
# # xpath_detail5 = '//div[@class="newscontent"]'
# # xpath_detail6 = '//div[@class="main_lt"]'
# xpath1= '//*[@id="comm_span"]/span'
# # #文章标题
# # xpath_detail7= '//div[@class="newscontent"]/h1'
# url_news = tree.xpath(xpath1)
# # print(url6)
# print(url_news)
# # for i in url_news:
# #     print(i.text)
