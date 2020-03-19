from scrapy import cmdline
import os
#
c = os.getcwd()
print(c)
os.chdir('/home/lis/Desktop/test/NewsSpider-master/scrapyspider/spiders')
cmdline.execute("scrapy crawl thepaper_all".split())
