#!/usr/bin/env python
# -*- coding: utf-8 -*-


def analyze(text):
	text = text.lower()
	for c in ':;,.!?[]7531902468':
		text = text.replace(c, '')
	res = {}
	for word in text.split(' '):
		if word in res:
			res[word] += 1
		else:
			res[word] = 1
	tlist = []
	for k, v in res.iteritems():
		tlist.append((k, v))
	tlist.sort(key=lambda tup: tup[1])
	return tlist


