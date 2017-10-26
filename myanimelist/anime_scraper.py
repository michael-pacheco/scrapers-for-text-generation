import scrapy, time

class MALScraper(scrapy.Spider):
    def __init__(self, *args, **kwargs):
        self.last_page = 0
        self.alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        self.file = open("anime_names.txt", "w+")
        super(MALScraper, self).__init__(*args, **kwargs)

    name = "MALScraper"
    start_urls = ["https://myanimelist.net/anime.php?letter=A"]


    def parse(self, response):
        #cycle through anime names from the webpage using a selector with css-style syntax
        #SET_SELECTOR = 'a.hoverinfo_trigger'

        #iterate over them and write to file
        for selector in response.css('strong::text'):
            self.file.write(selector.extract()+"\n")

        #find the number of the last page
        if self.last_page == 0:
            try:
                self.last_page = response.css('span.bgColor1 >a::text')[-1].extract()
            except:
                pass

        #find what page number we're on
        current_page_list = 0
        try:
            current_page_list = int(str(response.url).split("&show=")[1])
        except:
            pass

        #MAL paginates anime names by 50 animes per page
        #so if the current page number * 50 is not equal to the amount in our URL, we add 50 to our url to go to the next page
        #else the last page number is equal to our page number * 50, then we move onto the next letter
        if self.last_page != 0 and (int(self.last_page)-1) * 50 != current_page_list:
            #time.sleep(2)
            yield scrapy.Request(
                str(str(response.url).split("&show=")[0])+"&show="+str(current_page_list+50),
                callback=self.parse
            )
        else:
            #time.sleep(2)
            self.last_page = 0
            temp_url = str(response.url).split("&show=")
            url_to_change = str(temp_url[0][:len(temp_url[0])-1])
            next_letter = self.alphabet[(self.alphabet.index(str(temp_url[0][len(temp_url[0])-1])))+1]

            new_url = url_to_change + next_letter
            yield scrapy.Request(
                new_url,
                callback=self.parse
            )

    def closed( self, reason ):
        self.file.close()
