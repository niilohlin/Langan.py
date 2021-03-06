#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wikipedia
import langan
import random
import database
import signal

class TimeoutException(Exception):
	pass

class Crawler:
	def __init__(self):
		self.tolerance = 1000
		self.timeout = 20
		self.times = 1000

	@staticmethod
	def random_language():
		return random.choice(['en', 'fr', 'de', 'es', 'sv',
					'ru', 'it', 'pt', 'nl',
					'pl', 'ja', 'vi', 'zh', 'uk',
					'war', 'ceb', 'ca', 'no', 'fi', 'fa',
					'cs', 'ko', 'hu', 'ar', 'ro', 'ms'])

	def start(self):
		def timeout_handler(signum, frame):
			raise TimeoutException()

		signal.signal(signal.SIGALRM,timeout_handler)
		signal.alarm(self.timeout)
		for i in range(self.times):
			try:
				lang = Crawler.random_language()
				wikipedia.set_lang(lang)
				p = wikipedia.page(wikipedia.random())
				if len(p.content) > self.tolerance:
					print "reading page: ", p.title
					print "in language: ", lang
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
	c.start()
