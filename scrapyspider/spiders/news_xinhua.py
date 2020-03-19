# -*- coding:utf-8 -*-
from scrapy.crawler import CrawlerProcess
from scrapy.spiders import CrawlSpider, Rule
from scrapyspider.spiders.fenci import Fenci
from scrapy.http import Request
import os
from scrapy import cmdline, selector

from scrapyspider.items import newsItem, commentItem
from scrapyspider.spiders.tools import tools_spider
spider_tools = tools_spider()
news_item = newsItem()
comment_item = commentItem()
fenci = Fenci()

import requests
import time
import json
from lxml import etree
import pymongo
import re
from scrapyspider.spiders.fenci import Fenci
fenci = Fenci()
# 主函数

class NewsxinhuaSpider(CrawlSpider):
    # 爬虫名称
    name = "xinhua"
    # 新华全网
    allowed_domains = ["http://m.xinhuanet.com/", 'http://www.xinhuanet.com']
    def start_requests(self):
        start_uids = [
            # 手机版新华网：
            '11147664',  # 财经        经济建设
            '113352',  # 时政         政治
            '11145724',  # 国际：      政治
            '11145727',  # 娱乐：      文化
            '11145722',  # 图片：      社会
            '11145737',  # 社区：错漏数据较     社会
            '11145726',  # 军事：nid =     政治
            '11145728',  # 体育：nid =     文化
            '11145729',  # 前沿：nid =     社会
            '11145730',  # 教育：nid =     社会
            '11145723',  # 网评：nid =     社会
            '11145725',  # 港澳台：nid =    政治
            '113207',  # 法治：nid =       政治
            '113321',  # 社会：nid =       社会
            '11145736',  # 文化：nid =     文化
            '11145731',  # 时尚           文化
            '11145732',  # 旅游：nid =     生态文明
            '11145733',  # 健康：nid =     社会
            '11145734',  # 汽车：nid =     经济
            '11145738',  # 房产：nid =     经济
            '11145735',  # 美食：nid =     文化
            '11145720',  # 阅读：nid =     文化
            '11153046',  # 科普：nid =     社会
            '11100474',  # 新华社新闻：       社会
            '113351',  # 滚动新闻：nid =     社会
            # 品牌栏目：
            '11146377',  # 学习进行时 报错keyError:'data‘

            '11146687',  # 各省市：北京：nid =
            '11146688',  # 天津：nid =
            '11146689',  # 河北：nid =
            '11146690',  # 山西：nid =
            '11146691',  # 辽宁：nid =
            '11146692',  # 吉林：需要特殊处理
            '11146693',  # 上海：需要特殊处理
            '11146694',  # 江苏：nid =
            '11146695',  # 浙江：nid =
            '11146696',  # 安徽：nid =
            '11146697',  # 福建：nid =
            '11146698',  # 江西：nid =
            '11146699',  # 山东：nid =
            '11146700',  # 河南：nid =
            '11146701',  # 湖北：nid =
            '11146702',  # 湖南：nid =
            '11146703',  # 广东：nid =
            '11146704',  # 广西: nid =
            '11146705',  # 海南：需要特殊处理
            '11146706',  # 重庆：nid =
            '11146707',  # 四川：nid =
            '11146708',  # 贵州：nid =
            '11146709',  # 云南空白新闻过多，需要特殊处理
            '11146710',  # 西藏：nid =
            '11146711',  # 陕西：nid =
            '11146712',  # 甘肃：nid =
            '11146713',  # 青海：nid =
            '11146714',  # 宁夏  ok
            '11146715',  # 新疆  ok
            '11146716',  # 内蒙古  OK
            '11146717',  # 黑龙江  OK

        ]
        dict_clumn = {
            # 手机版新华网：
            '11147664': '财经',
            '113352': '时政',
            '11145724': '国际',
            '11145727': '娱乐',
            '11145722': '图片',  # ：
            '11145737': '社区',  # ：nid =
            '11145726': '军事',  # ：nid =
            '11145728': '体育',  # ：nid =
            '11145729': '前沿',  # ：nid =
            '11145730': '教育',  # ：nid =
            '11145723': '网评',  # ：nid =
            '11145725': '港澳台',  # ：nid =
            '113207': '法治',  # ：nid =
            '113321': '社会',  # ：nid =
            '11145736': '文化',  # ：nid =
            '11145731': '时尚',  # ：nid =
            '11145732': '旅游',  # ：nid =
            '11145733': '健康',  # ：nid =
            '11145734': '汽车',  # ：nid =
            '11145738': '房产',  # ：nid =
            '11145735': '美食',  # ：nid =
            '11145720': '阅读',  # ：nid =
            '11153046': '科普',  # ：nid =
            '11100474': '新华社新闻',  # ：nid =
            '113351': '滚动新闻',  # ：nid =
            # 品牌栏目：
            '11146377': '学习进行时',  # ：nid =
            '11146687': '北京',  # 各省市：：nid =
            '11146688': '天津',  # ：nid =
            '11146689': '河北',  # ：nid =
            '11146690': '山西',  # ：nid =
            '11146691': '辽宁',  # ：nid =
            '11146692': '吉林',  # ：nid =
            '11146693': '上海',  # ：nid =
            '11146694': '江苏',  # ：nid =
            '11146695': '浙江',  # ：nid =
            '11146696': '安徽',  # ：nid =
            '11146697': '福建',  # ：nid =
            '11146698': '江西',  # ：nid =
            '11146699': '山东',  # ：nid =
            '11146700': '河南',  # ：nid =
            '11146701': '湖北',  # ：nid =
            '11146702': '湖南',  # ：nid =
            '11146703': '广东',  # ：nid =
            '11146704': '广西',  # : nid =
            '11146705': '海南',  # ：nid =
            '11146706': '重庆',  # ：nid =
            '11146707': '四川',  # ：nid =
            '11146708': '贵州',  # ：nid =
            '11146709': '云南',  # ：nid =
            '11146710': '西藏',  # ：nid =
            '11146711': '陕西',  # ：nid =
            '11146712': '甘肃',  # ：nid =
            '11146713': '青海',  # ：nid =
            '11146714': '宁夏',  # ：nid =
            '11146715': '新疆',  # ：nid = 1
            '11146716': '内蒙古',  #
            '11146717': '黑龙江',  #
        }
        global uid
        for uid in start_uids:

            strClumn = dict_clumn[uid]
            news_item['strColumn'] = strClumn
            if strClumn == "财经" or strClumn == "汽车" or strClumn == "房产":
                strClass = "经济建设"
                news_item['strClass'] = strClass
            elif strClumn == "时政" or strClumn == "国际" or strClumn == "军事" or strClumn == "港澳台" or strClumn == "法治":
                strClass = "政治建设"
                news_item['strClass'] = strClass
            elif strClumn == "" or strClumn == "" or strClumn == "" or strClumn == "":
                strClass = ''
                news_item['strClass'] = strClass

            for page in range(2, 20):
                a = page
                page = str(a)
                url = "http://qc.wa.news.cn/nodeart/list?nid=" + uid + "&pgnum=" + page + "&cnt=12&attr=63&tp=1&orderby=1&mulatt=1?&_=1573696338019&callback=Zepto1573696328621"

                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/51.0.2704.63 Safari/537.36'}
                # 请求url获取响应
                yield Request(url=url, headers=headers, callback=self.xinhua_parse, dont_filter=True)
                r = requests.get(url=url, headers=headers)
    def xinhua_parse(self,response):
        dict_clumn = {
            # 手机版新华网：
            '11147664': '财经',
            '113352': '时政',
            '11145724': '国际',
            '11145727': '娱乐',
            '11145722': '图片',  # ：
            '11145737': '社区',  # ：nid =
            '11145726': '军事',  # ：nid =
            '11145728': '体育',  # ：nid =
            '11145729': '前沿',  # ：nid =
            '11145730': '教育',  # ：nid =
            '11145723': '网评',  # ：nid =
            '11145725': '港澳台',  # ：nid =
            '113207': '法治',  # ：nid =
            '113321': '社会',  # ：nid =
            '11145736': '文化',  # ：nid =
            '11145731': '时尚',  # ：nid =
            '11145732': '旅游',  # ：nid =
            '11145733': '健康',  # ：nid =
            '11145734': '汽车',  # ：nid =
            '11145738': '房产',  # ：nid =
            '11145735': '美食',  # ：nid =
            '11145720': '阅读',  # ：nid =
            '11153046': '科普',  # ：nid =
            '11100474': '新华社新闻',  # ：nid =
            '113351': '滚动新闻',  # ：nid =
            # 品牌栏目：
            '11146377': '学习进行时',  # ：nid =
            '11146687': '北京',  # 各省市：：nid =
            '11146688': '天津',  # ：nid =
            '11146689': '河北',  # ：nid =
            '11146690': '山西',  # ：nid =
            '11146691': '辽宁',  # ：nid =
            '11146692': '吉林',  # ：nid =
            '11146693': '上海',  # ：nid =
            '11146694': '江苏',  # ：nid =
            '11146695': '浙江',  # ：nid =
            '11146696': '安徽',  # ：nid =
            '11146697': '福建',  # ：nid =
            '11146698': '江西',  # ：nid =
            '11146699': '山东',  # ：nid =
            '11146700': '河南',  # ：nid =
            '11146701': '湖北',  # ：nid =
            '11146702': '湖南',  # ：nid =
            '11146703': '广东',  # ：nid =
            '11146704': '广西',  # : nid =
            '11146705': '海南',  # ：nid =
            '11146706': '重庆',  # ：nid =
            '11146707': '四川',  # ：nid =
            '11146708': '贵州',  # ：nid =
            '11146709': '云南',  # ：nid =
            '11146710': '西藏',  # ：nid =
            '11146711': '陕西',  # ：nid =
            '11146712': '甘肃',  # ：nid =
            '11146713': '青海',  # ：nid =
            '11146714': '宁夏',  # ：nid =
            '11146715': '新疆',  # ：nid = 1
            '11146716': '内蒙古',  #
            '11146717': '黑龙江',  #
        }
        strClumn = dict_clumn[uid]
        news_item['strColumn'] = strClumn
        if strClumn == "财经" or strClumn == "汽车" or strClumn == "房产":
            strClass = "经济建设"
            news_item['strClass'] = strClass
        elif strClumn == "时政" or strClumn == "国际" or strClumn == "军事" or strClumn == "港澳台" or strClumn == "法治":
            strClass = "政治建设"
            news_item['strClass'] = strClass
        elif strClumn == "" or strClumn == "" or strClumn == "" or strClumn == "":
            strClass = ''
            news_item['strClass'] = strClass

        body1 = response.text
        r1 = body1[19:]
        r2 = r1[:-1]
        body2 = r2
        try:
            body3 = json.loads(body2)
            c = body3["data"]
            d = c["list"]
        except Exception as e:
            pass
        for i in d:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/51.0.2704.63 Safari/537.36'}
            s = i["Title"]
            url = i["LinkUrl"]

            strPickDate = time.asctime(time.localtime(time.time()))

            

            yield Request(url=url,callback=self.xinhua_detail,dont_filter=True)
    def xinhua_detail(self,response):
        # 转码
        strPickDate = time.asctime(time.localtime(time.time()))
        c = response.url
        # print(response.body)

        try:
            # print(response.text)
            content = response.text
        except Exception as e:
            pass
        tree = etree.HTML(content)
        pathtest_img = '//*[@id="p-detail"]/p//img/@src'
        pathtest_vedio = '//div[@class="m-detail"]//iframe/@src'
        path_html_page = '//*[@id="p-detail"]'

        def img_tool(pathtest_img):
            # 如果存在图片
            if tree.xpath(pathtest_img):
                strConSource = tree.xpath(pathtest_img)
                dict2 = dict(zip(range(len(strConSource)), strConSource))
                for dic_key in dict2:
                    dict2[dic_key] = dict2[dic_key]
                strContentSource = dict2
                return strContentSource
            # 存在视频
            elif tree.xpath(pathtest_vedio):
                strContentSource = tree.xpath(pathtest_vedio)
                return strContentSource
            # 如果图片视频都存在
            elif tree.xpath(pathtest_img) and tree.xpath(pathtest_vedio):
                strImg = tree.xpath(pathtest_img)
                strContentSource = {}
                return strContentSource
            else:
                strContentSource = ""
                return strContentSource

        xpath_htmlpage = '//*[@id="p-detail"]'


        strContentSource = img_tool(pathtest_img)
        if "world" in c:
            path_title = '//div[@class="h-title"]/text()'
            path_content = '//*[@id="p-detail"]/p/text()'
            xpath_htmlpage = '//*[@id="p-detail"]'
        elif "fortune" in c:
            path_title = '//div[@class = "h-title"]/text()'
            path_content = '//*[@id="p-detail"]//p/text()'
            xpath_htmlpage = '//*[@id="p-detail"]'

            if tree.xpath('//*[@id="p-detail"]//p/span/text()'):
                path_content = '//*[@id="p-detail"]//p/span/text()'
                xpath_htmlpage = '//*[@id="p-detail"]'
        elif "sike" in c:
            path_title = '//*[@id="totop"]/div[1]/div/h3/text()'
            path_content = '//*[@id="totop"]/div[2]/div/div/div[1]//p/text()'
            strContentSource = tree.xpath('//*[@id="attachment_219550521"]/a/img/@src/text')
            xpath_htmlpage = '//div[@class="txt_zw"]'
        elif "forum" in c:
            path_title = '//div[@class="de-zw mt15"]/h1/span/text()'
            path_content = '//*[@id="message_"]/text()'
            xpath_htmlpage = '//div[@class="de-tai"]'
        # TODO 待解决信息遗漏问题

        else:
            xpath_htmlpage = '//*[@id="p-detail"]'
            path_title = '//div[@class="h-title"]/text()'
            path_content = '//*[@id="p-detail"]/p/text()'
            if path_content == "":
                path_content = '//*[@id="p-detail"]/p/text()'
                if path_content == "":
                    path_content = '//*[@id="DH-PLAYERID"]/text()'
            if path_content == "" and "politics" in c:
                path_content = '//*[@id="content"]/p/text()'
                path_title = '//*[@id="conTit"]/h1/text()'
        # 创建可供查询节点

        htmlpage = response.xpath(xpath_htmlpage).extract()[0]
        
        strTitle = tree.xpath(path_title)
        strTitle = "".join(strTitle)
        strTitle = re.sub('\s', ' ', strTitle)

        # xpath获取新闻正文
        strCon = tree.xpath(path_content)
        strContent = "".join(strCon)
        strContent = re.sub('\s', ' ', strContent)
        if tree.xpath('//span[@class="h-time"]/text()'):
            tiem1 = tree.xpath('//span[@class="h-time"]/text()')
        if tree.xpath('//*[@id="pubtime"]'):
            tiem1 = tree.xpath('//*[@id="pubtime"]')
        try:
            strPubDate = tiem1[0]
        except Exception as e:
            strPubDate = ""
        strContent = str(strContent)
        list_words = fenci.tokenization(strContent)
        strTitle = str(strTitle)
        strPickDate = str(strPickDate)
        strPickUrl = str(response.url)
        strPubDate = str(strPubDate)
        strContentSource = str(strContentSource)
        # news_item['strClumn'] = strClumn
        news_item['strContent'] = strContent
        news_item['strTitle'] =strTitle
        news_item['strPickDate'] =strPickDate
        news_item['strPickUrl'] =strPickUrl
        news_item['strName'] ="新华网"
        news_item['strPubDate'] =strPubDate
        news_item['strType'] ='1'
        news_item['strCityCode'] ='000000'
        news_item['strArea'] ='中国'
        news_item['strCommentSource'] =strContentSource
        news_item['strId'] ='5da57a93f71846ace852457d'
        news_item['strCreatName'] ="商信政通"
        news_item['strState'] ='1'
        news_item['list_words'] =list_words
        news_item['html_page'] =htmlpage

        # print(news_item)
        yield news_item
if __name__ == '__main__':
    cmdline.execute('scrapy crawl xinhua'.split())








