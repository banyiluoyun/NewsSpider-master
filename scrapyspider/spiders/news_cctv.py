# -*- coding:utf-8 -*-
from scrapy.crawler import CrawlerProcess
from scrapy.spiders import CrawlSpider, Rule

from scrapyspider.spiders.fenci import Fenci

from scrapy.utils.project import get_project_settings
from lxml import etree
from scrapy.http import Request
import os
from scrapy import cmdline, selector

from scrapyspider.items import newsItem, commentItem
import re

from scrapyspider.spiders.tools import tools_spider
import json

import time

from scrapyspider.spiders.tools import dict_clumn_cctv1,dict_clumn_cctv2
spider_tools = tools_spider()
news_item = newsItem()
comment_item = commentItem()
fenci = Fenci()


class NewspengpaiSpider(CrawlSpider):
    # 爬虫名称
    name = "cctv"
    # 澎湃全网
    allowed_domains = ["http://news.cctv.com/"]

    # 新闻版
    def start_requests(self):
        # start_urls1 = ['channels']
        # for url in start_urls1:
        #     yield Request(url=url,callback=self.)
        # 新闻
        # 改版后的央视新闻网站主要站点格式一样，所以集中处理
        start_urls1 = [
            # 新闻
            'news',
            # 国内
            'china',
            # 国际
            'world',
            # 社会
            'society',
            # 法制
            'law',
            # 文娱
            'ent',
            # 科技
            'tech',
            # 生活
            'life',
            # 教育
            'edu',
        ]
        start_urls2 = []
        for i in start_urls1:
            news_item['strColumn'] = dict_clumn_cctv1[i]
            for page in range(1,8):
                page = str(page)
                url = "http://news.cctv.com/2019/07/gaiban/cmsdatainterface/page/" + i + '_' + page + '.jsonp'
                'http://news.cctv.com/2019/07/gaiban/cmsdatainterface/page/life_1.jsonp'
                yield Request(url=url,callback=self.parse_cctv_first,dont_filter=True)
        for url in start_urls2:
            print(url)
    def parse_cctv_first(self,response):
        dict_r = json.loads(response.text.split('{"data":')[1][:-2])
        news_list = dict_r['list']
        for i in news_list:
            url_detail = i['url']
            if 'photo' in url_detail:
                pass
            else:
                yield Request(url=url_detail,callback=self.parse_news,dont_filter=True)
    def parse_news(self,response):

        news_item['strPickUrl'] = response.url
        xpath_column = '//div[@class="nav_daohang"]/a[3]'
        # 带div的展示数据
        xpath_title = '//*[@id="title_area"]/h1'
        xpath_title2 = '//div[@class="cnt_bd"]/h1'
        try:
            strtitle = response.xpath(xpath_title).extract()[0]
        except Exception as e:
            strtitle = response.xpath(xpath_title2).extract()[0]
        if strtitle:
            # print(strtitle)
            news_item['strTitle'] = spider_tools.str_tool_html(strtitle)
        else:
            print('未能获取到标题')
        xpath_htmlpage ='//*[@id="content_area"]'
        try:
            html_page = response.xpath(xpath_htmlpage).extract()[0]
            news_item['html_page'] = html_page

        except Exception as e:
            pass

        xpath_info = '//div[@class="info"]'
        xpath_info2 = '//div[@class="function"]/span/i'
        xpath_bianji = '//div[@class="zebian"]'
        try:
            content_info = spider_tools.str_tool_html(response.xpath(xpath_info).extract()[0])
            # 发布时间戳
            strPubDate = content_info.split('|')[1]
            strPubDate =''.join(strPubDate.split())
            strPubDate = strPubDate.replace('年', "-")
            strPubDate = strPubDate.replace('月', '-')
            strPubDate = strPubDate.replace('日', ' ')
            news_item['strPubDate'] = strPubDate
            # 来源
            news_item['content_source'] = content_info.split("来源：")[1].split("|")[0]
        except Exception as e :
            content_info = spider_tools.str_tool_html(response.xpath(xpath_info2).extract()[0])
            print(content_info)
            # 发布时间戳
            strPubDate = ''.join((content_info.split(' ')[1] + content_info.split(' ')[2]).split())
            strPubDate = strPubDate.replace('年', "-")
            strPubDate = strPubDate.replace('月', '-')
            strPubDate = strPubDate.replace('日', ' ')
            news_item['strPubDate'] = strPubDate
            # 来源
            news_item['content_source'] = content_info.split("来源：")[1]
        # 采集时间戳
        # print(news_item['strPubDate'])
        news_item['strPickDate'] = time.asctime(time.localtime(time.time()))
        # 新闻分类
        news_item['strType'] = '1'
        # 来源网站，例如新浪微博，
        news_item['strName'] = '央视新闻'
        # 部委名称
        news_item['strDepartment'] = ''
        # 正文
        xpath_content = '//*[@id="content_area"]'
        xpath_content2 = '//*[@id="text_area"]'
        flash_str = 'varisHttps=location.href.substr(0,5)=="https"?"true"'
        flash_str2 = ';createVodPlayer(playerParas);'
        try:
            content_selector = spider_tools.str_tool_html(response.xpath(xpath_content).extract()[0])
            content_selector = ''.join(content_selector.split())
            if flash_str in content_selector:
                news_item['strContent'] = content_selector.split(flash_str,)[0] + content_selector.split(flash_str2)[1]
            else:
                news_item['strContent'] = content_selector
        except Exception as e:
            content_selector = spider_tools.str_tool_html(response.xpath(xpath_content2).extract()[0])
            content_selector = ''.join(content_selector.split())
            if flash_str in content_selector:
                news_item['strContent'] = content_selector.split(flash_str,)[0] + content_selector.split(flash_str2)[1]
            else:
                news_item['strContent'] = content_selector
        # news_item['strContent'] = content_selector
        news_item['list_words'] = fenci.tokenization(news_item['strContent'])
        # 地区代码，默认000000
        news_item['strCityCode'] = '000000'
        # 地区，默认中国
        news_item['strArea'] = '中国'
        # 新闻分类的5大类
        news_item['strClass'] = ''
        # targetid
        news_item['strId'] = "5e539241ced9a5fad8cf75cd"
        news_item['strTargetId'] = ''
        # templateurl, 不存在默认为空
        xpath_img = '//*[@id="content_area"]/p/img/@src'
        strCommentSource = response.xpath(xpath_img).extract()
        img_list = []
        img_url_dict = {}
        for img_url in strCommentSource:
            for i in range(len(strCommentSource)):
                img_str = "img" + str(i)
                img_url_dict[img_str] = img_url
        img_list.append(img_url_dict)
        news_item['strCommentSource'] = img_list
        news_item['strCommentTemplateUrl'] = ''
        # 新闻评论
        news_item['strComment'] = ''
        # 阅读数
        news_item['intReadNum'] = ''
        # 状态
        news_item['strState'] = '1'
        # 转发数
        news_item['intTranspondNum'] = ''
        # 点赞数
        news_item['intUpNum'] = ''
        # 评论数
        news_item['intCommentNum'] = ""
        # 创建者名称
        news_item['strCreatName'] = '商信政通'



        yield news_item

if __name__ == '__main__':
    cmdline.execute('scrapy crawl cctv'.split())