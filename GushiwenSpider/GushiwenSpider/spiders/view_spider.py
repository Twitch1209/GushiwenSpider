# _*_ coding:utf8 _*_

from scrapy_redis.spiders import RedisSpider
from scrapy.loader import ItemLoader
from GushiwenSpider.items import ViewItem
from scrapy.crawler import CrawlerProcess


class ViewSpider(RedisSpider):
    """
    提取View页面主要内容：
    作品名称、作者、朝代、作品正文、翻译链接
    链接部分提交到redis，供爬虫fanyi_spider爬取
    """
    name = 'view_spider'
    redis_key = 'view:start_urls'
    custom_settings = {
        'ITEM_PIPLINES':{
          'GushiwenSpider.piplines.ParseViewPipline':300
        },
    }

    def parse(self, response):
        view_item = ItemLoader(item=ViewItem(), response=response)
        view_item.add_css('poetry_name', 'div.main3 div.left div.sons div.cont h1::text')
        view_item.add_value('poetry_link', response.url)
        view_item.add_css('poetry_dynasty', 'div.main3 div.left div.sons div.cont p a::text')
        view_item.add_css('poetry_author', 'div.main3 div.left div.sons div.cont p a::text')
        view_item.add_xpath('poetry_fanyi', '//div[@class="left"]/div[@id="fanyi1"]/div[@class="contyishang"]/p/text()')
        view_item.add_xpath('poetry_shangxi', '//div[@id="shangxi4"]/div[@class="contyishang"]/p/text()"]/p/text()')

        return view_item.load_item()


if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(ViewSpider)
    process.start()
