# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field

class newsItem(Item):   # 新闻内容包含以下属性
    _id = Field()  # 微博id
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

