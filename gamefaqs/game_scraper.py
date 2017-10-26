import scrapy, time

class GameScraper(scrapy.Spider):
    def __init__(self, *args, **kwargs):
        self.last_page = 0
        self.alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        self.consoles = []
        self.urls_scraped = 0
        self.console_iteration = 0
        self.file = open("game_names.txt", "w+")
        super(GameScraper, self).__init__(*args, **kwargs)

    name = "GameScraper"
    start_urls = ["https://www.gamefaqs.com/games/systems"]


    def parse(self, response):
        #if we're at the first url, scrape all the console names
        if self.urls_scraped == 0:
            for selector in response.css('td>a::attr(href)'):
                if "user" not in selector.extract():
                    self.consoles.append((selector.extract()).replace("/", ""))

            self.consoles = list(set(self.consoles))
            split_url = response.url.split("games")
            modified_url = split_url[0] + self.consoles[self.console_iteration] + "/category/999-all"
            self.urls_scraped+=1
            yield scrapy.Request(
                modified_url,
                callback=self.parse
            )

        else:
            #get page number if 0
            if self.last_page == 0:
                self.last_page = int((str((response.css('ul.paginate > li::text').extract())).split("of ")[1]).replace("']", ""))

            #get game names
            for selector in response.css('td.rtitle>a::text'):
                self.file.write(selector.extract()+"\n")

            if "?page=" in response.url:
                current_page = str(response.url).split("?page=")[1]
                #if current page is the last one
                if int(current_page) == int(self.last_page):
                    self.console_iteration+=1
                    #if iterations are done, exit
                    if self.console_iteration >= len(self.consoles):
                        return
                    current_console = self.consoles[(self.console_iteration)-1]
                    next_console = self.consoles[self.console_iteration]
                    modified_url = (response.url).replace("/"+current_console+"/", "/"+next_console+"/")
                    modified_url = (modified_url.split("?page="))[0]
                    self.urls_scraped+=1
                    self.last_page = 0
                    yield scrapy.Request(
                        modified_url,
                        callback=self.parse
                    )

                else:
                    next_page = int(((response.url).split("?page="))[1])+1
                    modified_url = (response.url).replace("="+str(next_page-1), "="+str(next_page))
                    self.urls_scraped+=1
                    yield scrapy.Request(
                        modified_url,
                        callback=self.parse
                    )
            else:
                modified_url = (response.url)+"?page=1"
                self.urls_scraped+=1
                yield scrapy.Request(
                    modified_url,
                    callback=self.parse
                )

    def closed( self, reason ):
        self.file.close()
