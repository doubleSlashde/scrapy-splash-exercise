# Automatically created by: shub deploy
from setuptools import setup, find_packages

setup(
    name='places_review_crawler',
    version='1.0',
    packages=find_packages(),
    package_data={
        'places_review_crawler': ['scripts/*.lua', 'resources/*.csv']},
    entry_points={
        'scrapy': ['settings = places_review_crawler.settings']},
    zip_safe=False
)
