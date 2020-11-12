import scrapy


class QuotesSpider(scrapy.Spider):
    name = "youla"

    def start_requests(self):
        urls = [
            'https://auto.youla.ru/sankt-peterburg/cars/used/ford/focus/',

        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for car_div in response.css('.SerpSnippet_snippetContent__d8CHK'):
            link = car_div.css('a.SerpSnippet_name__3F7Yu')
            title = link.css('::text').get()
            href = link.css('::attr(href)').get()
            raw_price = car_div.css('div.SerpSnippet_price__1DHTI')
            price = raw_price.css('::text').get()

            yield {
                'title': title,
                'href': href,
                'price': price,
            }
