import scrapy


class WorlodometerSpider(scrapy.Spider):
    name = "worldometer3"
    allowed_domains = ["www.worldometers.info"]
    start_urls = ["https://www.worldometers.info/world-population/population-by-country/"]

    def parse(self, response):
        countries = response.xpath('//td/a')
        for country in countries:
            country_name = country.xpath('.//text()').get()
            links = country.xpath('.//@href').get()
            absolute_link = response.urljoin(links)

            yield response.follow(url=absolute_link, callback=self.parse_data, meta={'country': country_name})

    def parse_data(self, response):
        Country = response.request.meta['country'] #importing any atribute from previous page
        rows = response.xpath('(//table[@class="table table-striped table-bordered table-hover table-condensed table-list"])[1]/tbody/tr')
        for row in rows:
            year = row.xpath(".//td[1]/text()").get()
            population = row.xpath(".//td[2]/strong/text()").get()
            yearly_change = row.xpath(".//td[3]/text()").get()
            yield {
                'Country': Country,
                'Year': year,
                'Population': population,
                'Yearly_change': yearly_change,
            }
