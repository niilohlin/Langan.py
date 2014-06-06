#!/usr/bin/env python
# -*- coding: utf-8 -*-


def analyze(text):
    text = text.lower()

    for c in ':;,.!?[]7531902468':
        text = text.replace(c, '')
    res = {}
    for word in text.split(' '):
        res.setdefault(word, 0)
        res[word] += 1

    tlist = [(k, v) for k, v in res.iteritems()]
    tlist.sort(key=lambda tup: tup[1])
    return tlist


