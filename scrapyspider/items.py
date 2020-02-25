# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


'''# 栏目名称
                    "strColumn": strClumn,
                    "strClass":strClass,
                    # 新闻正文
                    "strContent": strContent,
                    # 新闻标题
                    "strTitle": strTitle,
                    # 新闻采集时间
                    "strPickDate": strPickDate,
                    # 新闻链接
                    "strPickUrl": strPickUrl,
                    # 采集网站
                    "strName": "新华网",
                    # 新闻发布时间
                    "strPubDate": strPubDate,
                    # 新闻分类，
                    "strType": "1",
                    # 地区代码，默认000000,    标记id，默认为空，     地区，默认中国
                    "strCityCode": "000000",  "strArea": "中国",
                    # 图片以及视频url，list或者dict格式存储
                    "strCommentSource": strContentSource,
                    # 部委ID
                    "strId": "5da57a93f71846ace852457d",
                    # 创建者名称                 # 爬取状态
                    "strCreatName": "商信政通", "strState": "1",'''


class newsItem(Item):   # 新闻内容包含以下属性
    _id = Field()  # 微博id
    # 创建者名称
    strCommentSource = Field()
    strCreatName = Field()
    strColumn = Field()
    # weibo_url = Field()  # 微博URL
    strPickUrl = Field()  # 微博URL
    # created_at = Field()  # 微博发表时间
    strPubDate = Field()  # 微博发表时间
    # like_num = Field()  # 点赞数
    intUpNum = Field()  # 点赞数
    # repost_num = Field()  # 转发数
    strTranspondNum = Field()  # 转发数
    # comment_num = Field()  # 评论数
    intCommentNum = Field()  # 评论数
    # content = Field()  # 微博内容
    strContent = Field()  # 微博内容【
    strId = Field()
    # user_id = Field()  # 发表该微博用户的id
    strAccount = Field()  # 发表该微博用户的id
    tool = Field()  # 发布微博的工具
    image_url = Field()  # 图片
    video_url = Field()  # 视频
    strContentSource = Field()  # 视频和图片共享的字段
    origin_weibo = Field()  # 原始微博，只有转发的微博才有这个字段
    location_map_info = Field()  # 定位的经纬度信息
    # crawl_time = Field()  # 抓取时间戳
    strPickDate = Field()  # 抓取时间戳
    strTitle = Field()  # 新闻标题
    strType = Field()  # 新闻分类（聚类小类）
    strName = Field()  # 来源网站，例如新浪微博，
    strDepartment = Field()  # 部委名称
    strHasComment = Field()  # 是否有评论，默认1
    strCityCode = Field()  # 地区代码，默认000000
    strArea = Field()  # 地区，默认中国
    strClass = Field()  # 新闻分类的5大类，
    strTargetId = Field()  # targetid
    strCommentTemplateUrl = Field()  # templateurl, 不存在默认为空
    strComment = Field()  # 新闻url，默认为空
    intReadNum = Field()
    strState = Field()
    intTranspondNum = Field()
    html_page = Field()
    content_source = Field()

    # 文章标题
    title = Field()
    # 时间
    date = Field()
    # 正文
    content = Field()
    # 简介（20个字）
    abstract = Field()
    # 文章热度（参与数）
    heat = Field()
    # ID
    id = Field()
    # 链接
    url = Field()
    # 评论字典
    comments = Field()


class commentItem(Item):
    _id = Field()
    comment_user_id = Field()  # 评论用户的id
    strNick = Field()  # 评论用户id
    content = Field()  # 评论的内容
    strCommentText = Field()  # 评论的内容
    weibo_url = Field()  # 评论的微博的url
    strPickUrl = Field()  # 评论的微薄url
    # created_at = Field()  # 评论发表时间
    dtCommentData = Field()  # 评论发表时间
    # like_num = Field()  # 点赞数
    intUpNum = Field()  # 点赞数
    # crawl_time = Field()  # 抓取时间戳
    strPickDate = Field()  # 抓取时间戳
    intFansNum = Field()  # 评论人的粉丝数
    strArea = Field()  # 地区
    strCityCode = Field()  # 城市代码2
    strGender = Field()  # 评论人性别
    strId = Field()  # 新闻标题id
    strState = Field()

