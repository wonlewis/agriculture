# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from pathlib import PurePosixPath
from urllib.parse import urlparse

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline


class FeedtradePipeline:
    def process_item(self, item, spider):
        return item

class FeedtradeImagePipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None, *, item=None):
        name = PurePosixPath(urlparse(request.url).path).name
        return "files/" + PurePosixPath(urlparse(request.url).path).name