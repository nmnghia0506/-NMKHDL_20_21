import scrapy
import json

class collect_champagnes_info(scrapy.Spider):
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
    url = self.champagnes[self.champagne_count - 1]['champagne_url'] 
    yield scrapy.Request(url=url, callback=self.parse)     
     
    
  def parse(self, response):
    champagne_inf = {
      'Ma_sp': response.css('* > td > span::text').get(),
      'Ten_sp': response.xpath('*//div[1]/div[1]/div[3]/h1/text()').get(),
      'Gia': response.xpath('*//p/span/bdi/text()').get(),
      'Xuat_xu': response.xpath('*//tr/*[contains(text(), "Xuất")]/following-sibling::*/text()').extract_first(),
      'Nong_do': response.xpath('*//tr/*[contains(text(), "Nồng")]/following-sibling::*/text()').extract_first(),
      'Dung_tich': response.xpath('*//tr/*[contains(text(), "Dung")]/following-sibling::*/text()').extract_first(),
      'Giong_nho': response.xpath('*//tr/*[contains(text(), "Giống")]/following-sibling::*/text()').extract_first(),
      'Mau_sac': response.xpath('*//span/*[contains(text(), "Màu")]/following-sibling::text()').extract_first(),   
      'Loai_ruou': response.xpath('*//tr/*[contains(text(), "Loại")]/following-sibling::*/text()').extract_first(),
      'Thuong_hieu': response.xpath('//span/strong[contains(text(), "Thương")]/following-sibling::text() | *//tr/*[contains(text(), "Thương")]/following-sibling::*/text()').extract_first(),
      'Vung_lam_vang': response.xpath('*//tr/*[contains(text(), "Vùng")]/following-sibling::*/text()').extract_first(),
    }


    
    yield champagne_inf
    
    #if self.champagne_count < 5:  # test
    if self.champagne_count < len(self.champagnes):
      next_page_url = self.champagnes[self.champagne_count]['champagne_url'] 
      self.champagne_count += 1
      yield scrapy.Request(url=next_page_url, callback=self.parse) 