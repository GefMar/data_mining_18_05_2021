import scrapy


class AutoyoulaSpider(scrapy.Spider):
    name = 'autoyoula'
    allowed_domains = ['auto.youla.ru']
    start_urls = ['https://auto.youla.ru/']

    def _get_follow(self, response, selector_str, callback):
        for a_link in response.css(selector_str):
            url = a_link.attrib.get("href")
            yield response.follow(url, callback=callback)

    def parse(self, response):
        yield from self._get_follow(
            response,
            ".TransportMainFilters_brandsList__2tIkv a.blackLink",
            self.brand_parse
        )

    def brand_parse(self, response):
        yield from self._get_follow(
            response,
            ".Paginator_block__2XAPy a.Paginator_button__u1e7D",
            self.brand_parse
        )
        yield from self._get_follow(
            response,
            "a.SerpSnippet_name__3F7Yu.blackLink",
            self.car_parse
        )

    def car_parse(self, response):
        print(1)
