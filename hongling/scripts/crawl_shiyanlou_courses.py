import scrapy


class CoursesSpider(scrapy.Spider):
    name = 'courses'
    start_urls = ['https://www.shiyanlou.com/bootcamp/']

    def parse(self, response):
        for course in response.css('div.col-3'):
            yield {
                'name': course.css('div.course-body p::text').extract_first().strip(),
                'description': course.xpath('.//div[@class="course-body"]/p[2]/text()').extract_first(),
                'image_url': course.css('img::attr(src)').extract_first()
            }
