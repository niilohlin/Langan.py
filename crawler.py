#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wikipedia
import sqlite3
import langan

tolerance = 300
def main():
	while True:
		lang = ['en', 'fr', 'de', 'es', 'sv',
				'ru', 'it', 'pt', 'nl'].sample()
		wikipedia.set_lang(lang)
		p = wikipedia.page(wikipedia.random())
		if len(p.summary) > tolerance:
			langan.analyze(p.summary)
			pass
		




if __name__ == "__main__":
	main()
