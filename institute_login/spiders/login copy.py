import scrapy
from scrapy.http import FormRequest

class LoginSpider(scrapy.Spider):
    name = "login"

    start_urls = [
        "https://www.sdadmission.in/center/index.php?logout=1"
    ]

    def parse(self, response):
        return FormRequest.from_response(response, formdata = {
            "username" : "SD101",
            "password" : "SD101",
            "login.x"  : "25",
            "login.y"  : "48",
        }, callback=self.after_login)

    
    def after_login(self, response):
        for i in range(1,2501):
            url = 'https://www.sdadmission.in/center/update-center.php?id=' + str(i)
            yield scrapy.Request(url = url, callback = self.start_scrapping)

    def start_scrapping(self, response):
        name = response.css("#name::attr(value)").extract()
        director = response.css("#director::attr(value)").extract()
        state = response.css("#state::attr(value)").extract()
        city = response.css("#district::attr(value)").extract()
        address = response.css("#address::text").extract()
        pincode = response.css("#pincode::attr(value)").extract()
        mobile = response.css("#mobile::attr(value)").extract()
        email = response.css("#email::attr(value)").extract()
        website = response.css("#website::attr(value)").extract()

        #if name == '' and director == '' and state == '' and city == '' and address == '' and pincode == '' and mobile == '' and email == '' and website == '':
        if name[0] or director[0] or state[0] or city[0] or address[0] or pincode[0] or mobile[0] or email[0] or website[0]:
            yield {
                    "name" : name,
                    "director" : director,
                    "state" : state,
                    "city" : city,
                    "address" : address,
                    "pincode" : pincode,
                    "mobile" : mobile,
                    "email" : email,
                    "website" : website
                }
