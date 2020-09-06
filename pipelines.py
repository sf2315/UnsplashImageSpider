# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from urllib.request import urlopen


class UnsplashimagespiderPipeline:
    def process_item(self, item, spider):
        #每个item都代表一张要下载的图片
        print('----------' + item['image_id'])
        real_url = item['download'] + "?force=true"
        try:
            print("1  real_url:" + real_url)
            pass
            #打开URL对应的资源
            print("2")
            with urlopen(real_url) as result:
                #读取图片数据
                print("3")
                data = result.read()
                print("4  data:" + data)
                #打开图片文件
                with open("images/" + item['image_id'] + '.jpg', 'wb') as f:
                    #写入读取到的数据
                    print("5")
                    f.write(data)
                    print("6")
        except:
            print("下载图片错误" % item['image_id'])