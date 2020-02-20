# -*- coding:utf-8 -*-
from scrapy.crawler import CrawlerProcess
from scrapy.spiders import CrawlSpider, Rule
from scrapy.utils.project import get_project_settings
from lxml import etree
from scrapy.http import Request
from scrapy import cmdline, selector
from scrapyspider.items import newsItem,commentItem
import re
from scrapyspider.spiders.tools import tools_spider
spider_tools = tools_spider()

class NewspengpaiSpider(CrawlSpider):
    # 爬虫名称
    name = "pengpainews"
    #澎湃全网
    allowed_domains = ["https://www.thepaper.cn/" ]
    #新闻版
    def start_requests(self):
        start_urls = [
            # 时事栏目
            # 'https://www.thepaper.cn/channel_25950',
            #中南海
            'https://www.thepaper.cn/list_25488',

        ]
        for url in start_urls:
            if url == 'https://www.thepaper.cn/channel_25950':
                yield Request(url=url,callback=self.parse_lanmu, dont_filter=True)
            else:
                yield Request(url=url,callback=self.parse_detail,dont_filter=True)
    def parse_detail(self,response):
        xpath_shishi = '//div[@class="news_li"]/h2/a/@href'
        url_news = response.xpath(xpath_shishi).extract()
        print(url_news)
        for url in url_news:
            url_news1 = "http://www.thepaper.cn/" + url
            yield Request(url=url_news1,callback=self.parse_content,dont_filter=True)
    def parse_lanmu(self, response):

        resp = response
        tree = etree.HTML(resp.body)
        path_link = '//*[@id="listContent"]/div/h2/a/@href'
        url_news = tree.xpath(path_link)
        for url in url_news:
            url_news1 = "http://www.thepaper.cn/" + url
            yield Request(url=url_news1,callback=self.parse_content,dont_filter=True)
    def parse_content(self,response):
        news_item=newsItem()
        # news_item['strTitle']
        #带div的数据
        xpath_allpage = '//div[@class="newscontent"]'
        html_page = response.xpath(xpath_allpage).extract()[0]
        news_item['html_page'] = html_page
        #作者
        xpath_author = '//div[@class="clearfix"]'
        # 发布时间
        xpath_pubdate = '//div[@class="news_about"]/p[2]'
        news_item['strPubDate'] = spider_tools.str_tool_html(response.xpath(xpath_pubdate).extract()[0].split("来")[0])

        # 文章标题
        xpath_title = '//div[@class="newscontent"]/h1'
        title_html = response.xpath(xpath_title).extract()[0]
        title_result1 = spider_tools.str_tool_html(title_html)
        news_item['strTitle'] = title_result1



        # 文章正文
        xpath_detail4 = '//div[@class="news_txt"]'
        xpath_content = xpath_detail4
        content_selector = spider_tools.str_tool_html(response.xpath(xpath_content).extract()[0])
        news_item['strComment'] = content_selector

        #文章来源
        xpath_source = '//div[@class="news_about"]/p[1]'
        try:
            content_source = response.xpath(xpath_source).extract()[0]
            if content_source:
                content_source =spider_tools.str_tool_html(content_source)
                news_item['content_source'] = content_source
        except Exception as e:
            pass
        print(news_item)





if __name__ == "__main__":
    cmdline.execute('scrapy crawl pengpainews'.split())




    



