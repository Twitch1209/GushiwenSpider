

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.crawlerProcess import CrawlerProcess  # 让多个spider同时运行起来
from GushiwenSpider.items import GushiwenItem
import defines


class GushiwenSpider(CrawlSpider):
    name = 'gushiwen'
    allowed_domains = ['gushiwen.org']
    start_urls = defines.start_urls
    allowed_urls = defines.allowed_urls

    rules = [
        # 提取下一页链接,页面下方pages类中为小写字母。提取页面顺序：1、2、3、4、5....
        # deny是不想爬取的链接，callback：定义我们拿到可以爬取到的url后，要执行的方法，并传入每个链接的response内容（也就是网页内容）
        Rule(LinkExtractor(allow=allowed_urls, deny='.*baidu\.com'), callback='extract_view_urls', follow=True),
    ]

    custom_settings = {
        "ITEM_PIPELINES": {
            'GushiwenSpider.pipelines.GushiwenPipeline': 300
        },
    }

    def extract_view_urls(self, response):
        itemld = ItemLoader(item=GushiwenItem(), response=response)
        itemld.add_xpath('view_urls',
                         '//div[@class="main3"]/div[@class="left"]/div[@class="sons"]/div[@class="cont"]/p/a/@href')
        return itemld.load_item()


if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(GushiwenSpider)
    process.start()
