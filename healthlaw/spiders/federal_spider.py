# Spider to scrape whitehouse.gov

import scrapy
from healthlaw.items import FederalItem
from healthlaw.keywords import isInterestingLaw

class FederalSpider(scrapy.Spider):
    name = 'federal'
    start_urls = [
            'https://www.whitehouse.gov/briefing-room/legislation'
            ]

    def parse(self, response):
        for views_row in response.css('div.views-row'):
            federal_item = FederalItem()

            div_field_content = views_row.css('div.field-content')
            federal_item['disposition'] = div_field_content.css('strong::text').extract()[0]
            federal_item['date_of_disposition'] = div_field_content.css('span::attr(content)').extract()[0]
            # TODO: Continue if date of disposition is greater than 7 days

            h3_field_content = views_row.css('h3.field-content')
            federal_item['title'] = h3_field_content.css('a::text').extract()[0]
            federal_item['is_interesting_law'] = isInterestingLaw(federal_item['title'])
            federal_item['url_of_bill'] = h3_field_content.css('a::attr(href)').extract()[0]
            
            yield federal_item
