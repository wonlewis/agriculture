import scrapy
from scrapy.shell import inspect_response



class FeedTradeSpider(scrapy.Spider):
    name = "feedtrade_image"

    start_urls = ["https://res.feedtrade.com.cn/static//upload/g/caa6b83335f55c6e778019e9c1cb98a3-1712030385.png"]

    def parse(self, response):

        yield {
            'image_urls': ['https://res.feedtrade.com.cn/static//upload/g/caa6b83335f55c6e778019e9c1cb98a3-1712030385.png']
        }

    # def parse(self, response):
    #     # inspect_response(response, self)
    #     # image_url = response.xpath("//div[@class='prose-lg']/p/img")
    #     # image_url_attrib_src = image_url.attrib['src']
    #     yield {
    #         'image_urls': ["https://res.feedtrade.com.cn/static//upload/g/e0ba7d239b3674aa3e8e2a3b458406ed-1714103451.png"]
    #     }