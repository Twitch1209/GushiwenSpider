# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from mingshi.items import MingshiItem


class shiciSpider(CrawlSpider):
    name = 'mingshi'
    allowed_domains = ['www.shicimingju.com']

    # use start_requests replace start_urls to crawl many urls
    def start_requests(self):
        urls = ['http://www.shicimingju.com/chaxun/zuozhe/'+str(i)+'.html'for i in range(1,13033)]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # first rule to go to next page
    # second rule to get every urls , callback function to deal with messages in every urls
    rules = (
        Rule(LinkExtractor(allow=('/chaxun/zuozhe/\d_\d+\.html'))),
        Rule(LinkExtractor(allow=('/chaxun/list/\d+\.html')), callback='extract_view_urls', follow=False),

    )

    def extract_view_urls(self, response):
        items = []
        # define the fields for your item here like:
        item = MingshiItem()
        item['poetryName'] = response.xpath(
            '//div[@class="layui-container"]/div[@class="layui-row layui-col-space10"]/div[@class="layui-col-md8 layui-col-sm7"]/div[@class="shici-container www-shadow-card"]/h1/text()'
        ).extract()
        item['poetryDynasty'] = response.xpath(
            '//div[@class="layui-container"]/div[@class="layui-row layui-col-space10"]/div[@class="layui-col-md8 layui-col-sm7"]/div[@class="shici-container www-shadow-card"]/div[@class="shici-info"]/text()'
        ).extract()
        item['poetryAuthor'] = response.xpath(
            '//div[@class="layui-container"]/div[@class="layui-row layui-col-space10"]/div[@class="layui-col-md8 layui-col-sm7"]/div[@class="shici-container www-shadow-card"]/div[@class="shici-info"]/a/text()'
         ).extract()
        item['poetryBody'] = response.xpath(
            '//div[@class="layui-container"]/div[@class="layui-row layui-col-space10"]/div[@class="layui-col-md8 layui-col-sm7"]/div[@class="shici-container www-shadow-card"]/div[@class="shici-content"]/text()'
        ).extract()
        item['poetryAnalysis'] = response.xpath(
            '//div[@class="layui-container"]/div[@class="layui-row layui-col-space10"]/div[@class="layui-col-md8 layui-col-sm7"]/div[@class="shici-container www-shadow-card"]/div[@class="shangxi-container"]/text()'
        ).extract()
        items.append(item)
        return items





