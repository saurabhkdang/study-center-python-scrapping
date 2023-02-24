import scrapy
from scrapy.http import FormRequest

class LoginSpider(scrapy.Spider):
    name = "login"

    start_urls = [
        "https://www.rpshiksha.org/center/index.php?logout=1"
    ]

    def parse(self, response):
        return FormRequest.from_response(response, formdata = {
            "username" : "RPS101",
            "password" : "RPS101",
            "login.x"  : "57",
            "login.y"  : "40",
        }, callback=self.after_login)

    
    def after_login(self, response):
        for i in range(1105,1170):
            url = 'https://www.rpshiksha.org/center/update-center-detail.php?id=' + str(i)
            yield scrapy.Request(url = url, callback = self.start_scrapping)

    def start_scrapping(self, response):
        institute_name = response.css("#institute_name::attr(value)").extract()
        director = response.css("#director::attr(value)").extract()
        phone = response.css("#phone::attr(value)").extract()
        mobile = response.css("#mobile::attr(value)").extract()
        email = response.css("#email::attr(value)").extract()
        website = response.css("#website::attr(value)").extract()
        address = response.css("#address::text").extract()
        city = response.css("#district::attr(value)").extract()
        state = response.css("#state::attr(value)").extract()
        pincode = response.css("#pincode::attr(value)").extract()
        remarks = response.css("#remarks::text").extract()

        if institute_name[0] or director[0] or state[0] or city[0] or address[0] or pincode[0] or phone[0] or mobile[0] or email[0] or website[0] or remarks[0]:
            yield {
                    "institute_name" : institute_name,
                    "director" : director,
                    "phone" : phone,
                    "mobile" : mobile,
                    "email" : email,
                    "website" : website,
                    "address" : address,
                    "city" : city,
                    "state" : state,
                    "pincode" : pincode,
                    "remarks" : remarks,
                }
