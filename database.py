#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

setup_table = '''create table Stats (
cc char(3) not null,
char char(1) not null,
occ int not null,
primary key (cc, char));'''
path = 'database.db'

old_copy = None

def get_all(path='database.db'):
	conn = sqlite3.connect(path)
	resrow = {}
	for row in conn.execute('select * from Stats'):
		if row[0] in resrow:
			resrow[row[0]][row[1]] = row[2]
		else:
			resrow[row[0]] = {row[1]: row[2]}
	old_copy = resrow
	conn.close()
	return resrow


def _handler(option, db, path):
	conn = sqlite3.connect(path)
	for lang, langfreq in db.iteritems():
		for char, occ in langfreq.iteritems():
			if option == 'set':
				conn.execute(" \
				insert into Stats values (?, ?, ?) \
				", (lang, char, occ))
			elif option == 'update':
				conn.execute("update Stats set occ = ? where \
				cc = ? and char = ?",  (occ, lang, char))
	conn.commit()
	conn.close()


def set_all(db, path):
	_handler('set', db, path)

def update(db, path):
	_handler('update', db, path)

def diff(new, old):
	"""Assume new is a full member of old, i.e. none is deleted
	return the values that needs update and new values in a
	tuple of hashes
	"""
	update = {}
	insert = {}
	for lang, freq in new.iteritems():
		if lang in old:
			for char, occ in freq.iteritems():
				if char in old[lang]:
					if not occ == old[lang][char]:

						if lang in update:
							update[lang][char] = occ
						else:
							update[lang] = {char: occ}
					
				else:
					if lang in insert:
						insert[lang][char] = occ
					else:
						insert[lang] = {char: occ}
		else:
			insert[lang] = freq

	return insert, update


def merge(first, second):
	res = {}
	for lang, freq in second.iteritems():
		if lang in first:
			for char, occ in freq.iteritems():
				if char in first[lang]:
					if lang in res:
						res[lang][char] = occ
					else:
						res[lang] = {char: occ}
				else:
					if lang in res:
						res[lang][char] = occ
					else:
						res[lang] = {char: occ}
		else:
			res[lang] = freq

	for lang, freq in first.iteritems():
		if lang in second:
			for char, occ in freq.iteritems():
				if char in second[lang]:
					if lang in res:
						res[lang][char] = occ
					else:
						res[lang] = {char: occ}
				else:
					if lang in res:
						res[lang][char] = occ
					else:
						res[lang] = {char: occ}
		else:
			res[lang] = freq

	return res

def save(db):
	global old_copy
	if old_copy == None:
		old_copy = get_all()
	new, updatedb = diff(db, old_copy)
	set_all(new, path)
	update(updatedb, path)
	old_copy = merge(new, merge(update, old_copy))

