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
spider_tools = tools_spider()
import time

from scrapyspider.spiders.tools import dict_clumn_cctv1,dict_clumn_cctv2

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


        '''http://news.cctv.com/
            http://news.cctv.com/china/
            http://news.cctv.com/world/
            http://news.cctv.com/society/
            http://news.cctv.com/law/
            http://news.cctv.com/edu/
            http://news.cctv.com/ent/
            http://news.cctv.com/tech/
            http://news.cctv.com/life/
'''
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
        ]
        start_urls2 = []
        for i in start_urls1:
            news_item['strColumn'] = dict_clumn_cctv1[i]
            for page in range(1,2):
                page = str(page)
                url = "http://news.cctv.com/2019/07/gaiban/cmsdatainterface/page/" + i + '_' + page + '.jsonp'
                'http://news.cctv.com/2019/07/gaiban/cmsdatainterface/page/life_1.jsonp'
                yield Request(url=url,callback=self.parse_cctv_first,dont_filter=True)
    def parse_cctv_first(self,response):
        dict_r = json.loads(response.text.split('{"data":')[1][:-2])
        news_list = dict_r['list']
        for i in news_list:
            # print(i)
            url_detail = i['url']
            title = i['title']
            news_item['strTitle'] = title
            if 'photo' in url_detail:
                pass
            else:
                yield Request(url=url_detail,callback=self.parse_news,dont_filter=True)
    def parse_news(self,response):
        news_item['strPickUrl'] = response.url
        xpath_column = '//div[@class="nav_daohang"]/a[3]'
        # 带div的展示数据
        xpath_htmlpage ='//*[@id="content_area"]'
        try:
            html_page = response.xpath(xpath_htmlpage).extract()[0]
            news_item['html_page'] = html_page

        except Exception as e:
            pass

        xpath_info = '//div[@class="info"]'
        xpath_bianji = '//div[@class="zebian"]'
        content_info = spider_tools.str_tool_html(response.xpath(xpath_info).extract()[0])
        news_item['strPubDate'] = content_info.split('|')[1]
        print(content_info)
        # 发布时间戳

        # 来源
        news_item['content_source'] = content_info.split("来源")[1].split("|")[0]
        '''
    "strPubDate": "2017-02-06 08:14",
  
    "content_source": "澎湃新闻记者 袁璐 发自安徽合肥 实习生 陈思文",
    
    
   '''
        # 采集时间戳
        news_item['strPickDate'] = time.asctime(time.localtime(time.time()))
        # 新闻分类
        news_item['strType'] = '1'
        # 来源网站，例如新浪微博，
        news_item['strName'] = '澎湃新闻'
        # 部委名称
        news_item['strDepartment'] = ''

        # 正文
        xpath_content = '//*[@id="content_area"]'
        try:
            content_selector = spider_tools.str_tool_html(response.xpath(xpath_content).extract()[0])
        except Exception as e:
            pass
        news_item['strContent'] = content_selector
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













if __name__ == '__main__':
    cmdline.execute('scrapy crawl cctv'.split())