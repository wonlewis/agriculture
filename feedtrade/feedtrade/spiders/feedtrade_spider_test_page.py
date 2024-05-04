import scrapy
from scrapy.shell import inspect_response



class FeedTradeSpider(scrapy.Spider):
    name = "feedtrade_page"

    start_urls = ["https://www.feedtrade.com.cn/news/feedmarket/"]

    def parse(self, response):

        day_report_link = response.xpath("//div[@class='category-article-page-list']/ul/li/a")
        yield from response.follow_all(day_report_link, self.parse_day_report)

    def parse_day_report(self, response):
        image_url = response.xpath("//div[@class='prose-lg']/p/img/@src").get()
        yield {
            'image_urls': [image_url]
        }

    # def parse(self, response):
    #     # inspect_response(response, self)
    #     # image_url = response.xpath("//div[@class='prose-lg']/p/img")
    #     # image_url_attrib_src = image_url.attrib['src']
    #     yield {
    #         'image_urls': ["https://res.feedtrade.com.cn/static//upload/g/e0ba7d239b3674aa3e8e2a3b458406ed-1714103451.png"]
    #     }