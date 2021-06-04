from urllib.parse import urljoin
from scrapy import Selector
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose


def clear_price(price: str) -> float:
    try:
        result = float(price.replace("\u2009", ""))
    except ValueError:
        result = None
    return result


def get_characteristics(item: str):
    selector = Selector(text=item)
    data = {
        "name": selector.xpath("//div[contains(@class, 'AdvertSpecs_label')]/text()").get(),
        "value": selector.xpath("//div[contains(@class, 'AdvertSpecs_data')]//text()").get(),
    }
    return data


def create_author_link(author_id: str) -> str:
    author = ""
    if author_id:
        author = urljoin("https://youla.ru/user/", author_id)
    return author


class AutoyoulaLoader(ItemLoader):
    default_item_class = dict
    url_out = TakeFirst()
    title_out = TakeFirst()
    price_in = MapCompose(clear_price)
    price_out = TakeFirst()
    descriptions_out = TakeFirst()
    characteristics_in = MapCompose(get_characteristics)
    author_in = MapCompose(create_author_link)
    author_out = TakeFirst()
