import scrapy


class Review(scrapy.Item):
    place_id = scrapy.Field()
    review_text = scrapy.Field()
    review_date = scrapy.Field()
    user_name = scrapy.Field()
    user_profile = scrapy.Field()
