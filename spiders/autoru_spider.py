import scrapy


# функция для очистки стоимости
def clean_price(text):
    digits = [symbol for symbol in text if symbol.isdigit()]
    cleaned_text = ''.join(digits)
    if not cleaned_text:
        return None
    return int(cleaned_text)


class QuotesSpider(scrapy.Spider):
    name = "auto"

    def start_requests(self):
        urls = [
            'https://auto.ru/sankt-peterburg/cars/ford/focus/all/',

        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for car_div in response.css('.ListingItem-module__main'):
            link = car_div.css('a.ListingItemTitle-module__link')
            title = link.css('::text').get()
            href = link.css('::attr(href)').get()
            raw_price = car_div.css('div.ListingItemPrice-module__content')
            price = raw_price.css('span::text').get()
            clened_price = price and clean_price(price) or None

            img_urls = car_div.css('.Brazzers__image::attr(data-src)').getall()
            yield {
                'title': title,
                'href': href,
                'price': clened_price,
                'img': [response.urljoin(img) for img in img_urls],
            }
