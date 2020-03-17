# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html
'''中间件保持不变即可'''
import base64
import logging

from scrapy import signals


class ScrapyspiderSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

class RedirectMiddleware(object):
    def process_response(self, request, response, spider):
        http_code = response.status
        if http_code == 418 or http_code==429:
            spider.logger.error('ip 被封了!!!请更换ip,或者停止程序...')
            return request
        else:
            return response

logger = logging.getLogger(__name__)
# 隧道id和密码
tid = "t17732540351546"
password = "9myov9n2"
# 隧道host和端口
tunnel_master_host = "tps176.kdlapi.com"
tunnel_master_port = 15818
# 备用隧道host和端口
tunnel_slave_host = "tps172.kdlapi.com"
tunnel_slave_port = 15818
# 切换阀值
threshold = 2

# 代理中间件
class ProxyDownloadMiddleware(object):

    def process_request(self, request, spider):
        global threshold
        if threshold > 0:
            host, port = tunnel_master_host, tunnel_master_port
        else:
            host, port = tunnel_slave_host, tunnel_slave_port
        if request.url.startswith("http://"):
            proxy_url = 'http://{host}:{port}'.format(host=host, port=port)
        elif request.url.startswith("https://"):
            proxy_url = 'https://{host}:{port}'.format(host=host, port=port)
        request.meta['proxy'] = proxy_url  # 设置代理
        logger.debug("using proxy: {}".format(request.meta['proxy']))
        # 隧道代理需要进行身份验证
        #
        # 用户名和密码需要先进行base64编码，然后再赋值
        username_password = "{tid}:{password}".format(tid=tid, password=password)
        b64_username_password = base64.b64encode(username_password.encode('utf-8'))
        request.headers['Proxy-Authorization'] = 'Basic ' + b64_username_password.decode('utf-8')
        threshold -= 1
        return None


