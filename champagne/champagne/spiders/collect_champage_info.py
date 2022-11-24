import scrapy
import json

class collect_player_info(scrapy.Spider):
  name='champagnes_info'

  custom_settings = {
        'DOWNLOAD_DELAY': 0.5 ,
        'ROBOTSTXT_OBEY' : True,
    }
  
  def __init__(self):
    try:
      with open('dataset/champagne_urls.json') as f:
        self.champagnes = json.load(f)
      self.champagne_count = 1
    except IOError:
      print("File not found")

  def start_requests(self):
    url = self.champagnes[self.player_count - 1]['champagne_url'] 
    yield scrapy.Request(url=url, callback=self.parse)     
     
    
  def parse(self, response):


    
    yield champagne_inf
    
    if self.champagne_count < len(self.champagnes):
        next_page_url = self.players[self.champagne_count]['champagne_url'] 
        self.champagne_count += 1
        yield scrapy.Request(url=next_page_url, callback=self.parse) 