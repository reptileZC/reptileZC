# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EastmoneyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    基金代码 = scrapy.Field()
    基金简称 = scrapy.Field()
    日期 = scrapy.Field()
    单位净值 = scrapy.Field()
    累计净值 = scrapy.Field()
    日增长率 = scrapy.Field()
    近1周 = scrapy.Field()
    近1月 = scrapy.Field()
    近3月 = scrapy.Field()
    近6月 = scrapy.Field()
    近1年 = scrapy.Field()
    近2年 = scrapy.Field()
    近3年 = scrapy.Field()
    今年来 = scrapy.Field()
    成立来 = scrapy.Field()
    手续费 = scrapy.Field()


