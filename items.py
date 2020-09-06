# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class UnsplashimagespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #保存图片
    image_id = scrapy.Field()
    #保存图片下载地址
    download = scrapy.Field()
