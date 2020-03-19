# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
import pymongo
from pymongo.errors import DuplicateKeyError
from scrapyspider.items import newsItem,commentItem
from scrapyspider.settings import DB_NAME1,DB_NAME2,LOCAL_MONGO_HOST1,LOCAL_MONGO_PORT1,local_mongo_host,local_mongo_port

class MongoDBPipeline(object):
    def __init__(self):
        client1 = pymongo.MongoClient(LOCAL_MONGO_HOST1,LOCAL_MONGO_PORT1)
        client2 = pymongo.MongoClient(local_mongo_host,local_mongo_port)
        db = client1[DB_NAME1]
        db2 = client2[DB_NAME2]
        self.Information = db2["weibo_Information"]
        # self.Tweets = db["Tweets"]
        # 入库公司服务器地址
        self.Tweets = db["suncn_news_pickfromofficial"]
        self.Comments = db["suncn_news_comment"]
        # 入库本机
        # self.Tweets = db2["suncn_news_pickfromunofficial"]
        # self.Comments = db2["suncn_news_comment"]

        # self.Comments = db["suncn_news_comment"]
        self.Relationships = db2["weibo_Relationships"]

    def process_item(self, item, spider):
        """ 判断item的类型，并作相应的处理，再入数据库 """
        if isinstance(item, newsItem):
            self.insert_item(self.Tweets, item)

        elif isinstance(item, commentItem):
            self.insert_item(self.Comments, item)
        return item

    @staticmethod
    def insert_item(collection, item):
        try:
            collection.update({'strPickUrl':item.get('strPickUrl')},{'$set':item}, True)
        except DuplicateKeyError:
            """
            说明有重复数据
            """
            pass


class MongoDBPipeline1(object):
    def __init__(self):
        client1 = pymongo.MongoClient(LOCAL_MONGO_HOST1,LOCAL_MONGO_PORT1)
        client2 = pymongo.MongoClient(local_mongo_host,local_mongo_port)
        db = client1[DB_NAME1]
        db2 = client2[DB_NAME2]
        self.Information = db2["weibo_Information"]

        # 入库本机
        self.Tweets = db2["suncn_news_pickfromofficial"]
        self.Comments = db2["suncn_news_comment"]

        # self.Comments = db["suncn_news_comment"]
        self.Relationships = db2["weibo_Relationships"]

    def process_item(self, item, spider):
        """ 判断item的类型，并作相应的处理，再入数据库 """
        if isinstance(item, newsItem):
            self.insert_item(self.Tweets, item)

        elif isinstance(item, commentItem):
            self.insert_item(self.Comments, item)
        return item

    @staticmethod
    def insert_item(collection, item):
        try:
            collection.update({'strPickUrl':item.get('strPickUrl')},{'$set':item}, True)
        except DuplicateKeyError:
            """
            说明有重复数据
            """
            pass

