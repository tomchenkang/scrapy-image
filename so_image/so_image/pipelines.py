# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from urllib.request import urlretrieve
from os.path import join
import os

class SoImagePipeline(object):
	def process_item(self, item, spider):
		path = spider.settings.get('IMAGES_STORE')
		path1 = path + join(item['title'], item['name'] + '.' + item['index'] + '.jpg')
		mpath = path + item['title']
		if os.path.exists(mpath):
		    pass
		else:
		    os.mkdir(mpath)
		urlretrieve(item['image_urls'], path1)
		return item
