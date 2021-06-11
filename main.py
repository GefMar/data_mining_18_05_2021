from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from gb_parse.spiders.youla import AutoyoulaSpider
from gb_parse.spiders.hh import HhRemoteSpider
from gb_parse.spiders.avito import AvitoRealEstateSpider


if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule("gb_parse.settings")
    crawler_process = CrawlerProcess(settings=crawler_settings)
    crawler_process.crawl(AvitoRealEstateSpider)
    crawler_process.start()
