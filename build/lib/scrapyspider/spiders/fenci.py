# -*-coding:utf-8-*-

import pymongo
import pandas as pd
import jieba.posseg as pseg
import codecs


class Fenci(object):
    def __init__(self):
        # 构建停词表
        stop_words = '/home/lis/Desktop/test/NewsSpider-master/scrapyspider/spiders/stop_words_cn.txt'
        stopwords = codecs.open(stop_words, 'r', encoding='utf8').readlines()
        self.stopwords = [w.strip() for w in stopwords]
        self.stop_flag = ['x', 'c', 'u', 'd', 'p', 't', 'uj', 'm', 'f', 'r']

    def tokenization(self, text):
        result = []
        words = pseg.cut(text)
        for word, flag in words:
            if flag not in self.stop_flag and word not in self.stopwords:
                result.append(word)
        return result


