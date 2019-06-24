from pkgutil import get_data

import scrapy.item
from scrapy_splash import SplashRequest
from w3lib.http import basic_auth_header

from places_review_crawler.items import Review


class PlacesDetailSpider(scrapy.Spider):
    name = 'places_review_spider'

    def __init__(self, *args, **kwargs):
        places_file = get_data('places_review_crawler', 'resources/place_ids.csv').decode('utf-8')
        self.place_ids = places_file.split('\r\n')
        self.LUA_SOURCE = get_data(
            'places_review_crawler', 'scripts/places_review_crawler.lua'
        ).decode('utf-8')
        super(PlacesDetailSpider, self).__init__(*args, **kwargs)

    def start_requests(self):
        for place_id in self.place_ids:
            yield SplashRequest(
                url='https://www.google.com/maps/place/?q=place_id:' + place_id,
                endpoint='execute',
                splash_headers={
                    'Authorization': basic_auth_header(self.settings['SPLASH_APIKEY'], ''),
                },
                args={
                    'wait': 0.5,
                    'timeout': 60,
                    'lua_source': self.LUA_SOURCE,
                },
                cache_args=['lua_source'],
            )

    def parse(self, response):
        review_items = response.css('.section-review-content')
        for review_item in review_items:
            yield Review({
                'place_id': response.url.split("place_id:")[1],
                'user_name': review_item.css('.section-review-title span::text').extract(),
                'user_profile': review_item.css(".section-review-titles-with-menu").xpath('a//@href').extract(),
                'review_text': review_item.css(".section-review-text::text").extract(),
                'review_date': review_item.css(".section-review-publish-date::text").extract()
            })
