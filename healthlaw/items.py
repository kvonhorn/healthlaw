# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FederalItem(scrapy.Item):
    disposition = scrapy.Field()    # Signed, Pending & posted, or Vetoed   TODO: Make an enum?
    date_of_disposition = scrapy.Field()
    title = scrapy.Field()
    url_of_bill = scrapy.Field()
    is_interesting_law = scrapy.Field()
    # NOTE: These two are useful if I pass through to url_of_bill and scrape them
    #bill_link = scrapy.Field()
    #bill_pdf_link = scrapy.Field()
