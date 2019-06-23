# -*- coding: utf-8 -*-

BOT_NAME = 'places_review_crawler'
SPIDER_MODULES = ['places_review_crawler.spiders']

CONCURRENT_REQUESTS = 1
AUTOTHROTTLE_ENABLED = True
DOWNLOAD_TIMEOUT = 90000
HTTPERROR_ALLOW_ALL = True

SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}

DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}

# Splash settings
SPLASH_URL = 'http://localhost:8050'
