# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoctorItem(scrapy.Item):
    physician_name = scrapy.Field()
    overall_score = scrapy.Field()
    review = scrapy.Field()
    ratings = scrapy.Field()
    review_date = scrapy.Field()
    hash_key = scrapy.Field()
