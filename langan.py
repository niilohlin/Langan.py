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
	for fk, fv in first.iteritems:
		if fk in second:
			res[fk] = abs(fv - second[fk])
	for sk, sv in second.iteritems:
		if sk in first and not sk in res:
			res[sk]= abs(sv - first[sk])
	return res

def _sum(compared):
	sum = 0
	for v in compared.itervalues:
		sum += v
	return sum

def _closest(listof, db):
	for lang in listof:

