import scrapy


class WorlodometerSpider(scrapy.Spider):
    name = "worldometer2"
    allowed_domains = ["www.worldometers.info/"]
    start_urls = ["https://www.worldometers.info/world-population/population-by-country/"]

    def parse(self, response):
        #title = response.xpath('//h1/text()').get()
        countries = response.xpath('//td/a')

        for country in countries:
            country_name=country.xpath('.//text()').get()
            links = country.xpath('.//@href').get()
            absolute_link=response.urljoin(links)

            yield {
                # 'titles':title,
                'country name':country_name,
                #'link': links,
                'links':scrapy.Request(url=absolute_link),
            }
            print('\n')


