# -*- coding: utf-8 -*-
import scrapy
import re
import datetime
from scrapy.loader import ItemLoader
from ..items import DoctorItem


class DoctorReviewSpider(scrapy.Spider):
    name = 'doctor_review'
    allowed_domains = ['doctor.com']
    start_urls = ['https://www.doctor.com/Dr-Heather-Pulaski']

    def parse(self, response):

        physician_name = response.css(
            'div.name-bio--name h2::text').extract_first().strip()
        review_number = response.css('a#s-stats-rlink').extract_first()
        review_numbers = re.findall(r'\d+', review_number)

        if ''.join(review_numbers) != '0':

            overall = response.css(
                'div.pic-stats--stats div.star-rating::attr(class)').extract_first()
            overall_score = re.findall(r'\d+', overall)

        reviewNodes = response.xpath('//article[@class="review"]')

        for reviewText in reviewNodes:
            reviews = reviewText.css('div.review-text p::text').extract()
            review = ''.join(reviews)
            review = review.replace('“”', '').strip()

            rating = reviewText.css(
                'div.review-head div::attr(class)').extract_first()
            ratings = re.findall(r'\d+', rating)

            review_date = reviewText.css(
                'em.review-date::text').extract_first()
            review_date = datetime.datetime.strptime(
                review_date, '%m/%d/%Y').strftime('%Y-%m-%d')

            hash_key = reviewText.css('div.hidden::attr(id)').extract_first()

            l = ItemLoader(item=DoctorItem())

            l.add_value('physician_name', physician_name)
            l.add_value('overall_score', overall_score)
            l.add_value('review', review)
            l.add_value('ratings', ratings)
            l.add_value('review_date', review_date)
            l.add_value('hash_key', hash_key)
            print('\n\n\n', l.load_item())

            l.load_item()

            print('\n\n')
            # yield {'Physician Name': physician_name,
            #        'Overall Score': overall_score,
            #        'Review': review,
            #        'Review Rating': ratings,
            #        'Review Data': review_date,
            #        'Unique Key': hash_key
            #        }
            # print('\n\n')
