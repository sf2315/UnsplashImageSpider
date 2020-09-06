import scrapy,json
from UnsplashImageSpider.items import UnsplashimagespiderItem


class UnsplashImageSpider(scrapy.Spider):
    name = 'unsplash_image'
    allowed_domains = ['unsplash.com']
    start_urls = ['http://unsplash.com/napi/photos?page=1&per_page=12&order_by=latest']
    def __init__(self):
        self.page_index = 1
        
    def parse(self, response):
        #解析服务器响应的JSON字符串
        photo_list = json.loads(response.text)
        #遍历每张图片
        for photo in photo_list:
            item = UnsplashimagespiderItem()
            item['image_id'] = photo['id']
            item['download'] = photo['links']['download']
            yield item
            
        self.page_index += 1
        #获取下一页的链接
        next_link = 'https://unsplash.com/napi/photos?page=' + str(self.page_index) + '&per_page=12&order_by=latest'
        #继续获取下一页的图片
        yield scrapy.Request(next_link, callback=self.parse)
