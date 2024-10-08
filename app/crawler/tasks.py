import django_rq
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from .web_scraper.spiders.story_spider import StorySpider

def run_spider():
    process = CrawlerProcess(get_project_settings())
    process.crawl(StorySpider)
    process.start()

def enqueue_spider():
    queue = django_rq.get_queue('default')
    queue.enqueue(run_spider)