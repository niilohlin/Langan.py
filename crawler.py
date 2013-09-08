#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wikipedia
import langan
import random
import database
class Crawler:
	def __init__(self):
		self.tolerance = 300
		self.times = 200

	@staticmethod
	def random_language():
		return random.choice(['en', 'fr', 'de', 'es', 'sv',
					'ru', 'it', 'pt', 'nl',
					'pl', 'ja', 'vi', 'zh', 'uk'])

	def main(self):
		for i in range(self.times):
			try:
				lang = Crawler.random_language()
				wikipedia.set_lang(lang)
				p = wikipedia.page(wikipedia.random())
				print "reading page: ", p.title
				print "in language: ", lang
				if len(p.content) > self.tolerance:
					content = Crawler._clean(p.content)
					database.save({lang : langan.analyze(content)})
			except:
				pass
	@staticmethod
	def _clean(string):
		for c in "7531902468\n[]=().,?!\"\'":
			string = string.replace(c, '')
		return string




if __name__ == "__main__":
	c = Crawler()
	c.main()
