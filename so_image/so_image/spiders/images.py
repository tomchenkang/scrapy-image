# -*- coding: utf-8 -*-
import scrapy
import requests
from so_image.items import SoImageItem
import json


class ImagesSpider(scrapy.Spider):
	BASE_URL = "http://image.so.com/zj?ch=art&t1=1780&sn=%s&listtype=new&temp=1"
	Dbase_url = 'http://image.so.com/zvj?ch=art&id='
	start_index = 0
	MAX_DOWNLOAD_NUM = 120
	name = 'images'
	allowed_domains = ['image.so.com']
	start_urls = [BASE_URL%0,]
	
	def parse(self, response):
		data = requests.post(self.start_urls[0])
		infos = data.json()

		for info in infos['list']:
			detailurl = self.Dbase_url + info['id']
			yield response.follow(detailurl, callback=self.parse_more)				

		self.start_index += infos['count']
		if infos['count'] > 0 and self.start_index < self.MAX_DOWNLOAD_NUM:
			yield response.follow(self.BASE_URL%self.start_index)

	def parse_more(self, response):
		data = json.loads(response.body.decode())
		imageinfo = SoImageItem()
		for info in data['list']:
			imageinfo['image_urls'] = info['qhimg_url'] 
			imageinfo['name'] = info['pic_desc'].split(' ')[0]
			if '【' in imageinfo['name']:
				imageinfo['name'] = imageinfo['name'][1:-1]
			imageinfo['title'] = info['pic_title']
			imageinfo['index'] = str(info['index'])
			yield imageinfo