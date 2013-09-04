#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This prgam analyzes a text and tries to 
# guess what language it is written in

def analyze(text):
	"""Calculate the letterfrequency of each letter in 
	a string, and return it.
	"""
	text = text
	freq = _freq(text)
	return freq

def _freq(text):
	res = {}
	for c in text:
		if c in res:
			res[c] += 1
		else:
			res[c] = 1
	return res

def _compare(first, second):
	res = {}
	for fk, fv in first.iteritems():
		if fk in second:
			res[fk] = abs(fv - second[fk])
		else:
			res[fk] = fv

	for sk, sv in second.iteritems():
		if sk in first and not sk in res:
			res[sk] = abs(sv - first[sk])
		else:
			res[sk] = sv
	return res

def _sum(compared):
	sum = 0
	for v in compared.itervalues():
		sum += v
	return sum

def _map_hash_values(fun, myhash):
	res = {}
	for k, v in myhash.iteritems():
		res[k] = fun(v)
	return res

def _percentage(freq):
	s = float(_sum(freq))
	return _map_hash_values(lambda v : v / s, freq)

def closest(freq, db):
	"""Tries guess of which language the given freq
	is corresponding to. Returns a list of the language
	and the error rate. Smaller == better.
	"""
	freq = _percentage(freq)
	for i in xrange(len(db)):
		db[i][1] = _percentage(db[i][1])
	res = []
	for lang, langfreq in db:
		res.append([lang, _compare(freq, langfreq)])
	res = map(lambda x: [x[0],_sum(x[1])], res)
	smallest = res[0]
	for i in res:
		if i[1] < smallest[1]:
			smallest = i
	return smallest

def guess(text, db):
	"""Tries to guess the language of a given text"""
	return closest(analayze(text), db)



db = [['sv', analyze("okej nu blir det lite sveska i huset")],
		['en', analyze("okay well this is a little bit of english")]]
freq = analyze("och nu har vi lite sveska att leka med igen")
