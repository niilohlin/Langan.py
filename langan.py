#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This prgam analyzes a text and tries to
# guess what language it is written in

def analyze(text):
    """Calculate the letterfrequency of each letter in
    a string, and return it.
    """
    return n_grams(text, 1)

def n_grams(text, n):
    res = {}
    for i in range(len(text) - n + 1):
        if text[i:i + n] in res:
            res[text[i:i + n]] += 1
        else:
            res[text[i:i + n]] = 1
    return res

def _compare(first, second):
    res = {}
    for fk, fv in first.iteritems():
        if fk in second:
            res[fk] = abs(fv - second[fk])
        else:
            res[fk] = fv

    for sk, sv in second.iteritems():
        if not sk in first:
            res[sk] = sv

#    for sk, sv in second.iteritems():
#        if sk in first and not sk in res:
#            res[sk] = abs(sv - first[sk])
#            print "this is happening"
#        else:
#            res[sk] = sv
    return res

def _sum(compared):
    return sum(compared.itervalues())

def hashmap(fun, myhash):
    return {k: fun(v) for k, v in myhash.iteritems()}

def _percentage(freq):
    s = float(_sum(freq))
    return hashmap(lambda v : v / s, freq)

def _get_first(adict):
    for k, v in adict.iteritems():
        return k, v



def closest(freq, db):
    """Tries guess of which language the given freq
    is corresponding to. Returns a list of the language
    and the error rate. Smaller == better.
    """
    freq = _percentage(freq)

    prctage = {}
    for lang, langfreq in db.iteritems():
        prctage[lang] = _percentage(langfreq)
    #prctage = {lang: langfreq for lang, langfreq in db.iteritems()}

    compared = {}
    for lang, langfreq in prctage.iteritems():
        compared[lang] = _compare(freq, langfreq)

    summed = {}
    for lang, langfreq in compared.iteritems():
        summed[lang] = _sum(langfreq)

    smallest = _get_first(summed)
    for k, v in summed.iteritems():
        if v < smallest[1]:
            smallest = (k, v)
    return smallest

def compose(f, g, h):
    return lambda x: f(g(h(x)))
def partial(f, v):
    return lambda x: f(v, x)

# TODO benchmark this.
def functclosest(freq, db):
    """Tries guess of which language the given freq
    is corresponding to. Returns a list of the language
    and the error rate. Smaller == better.
    """
    compfreq = partial(_compare, _percentage(freq))
    superfun = compose(_sum, compfreq, _percentage)
    summed = {lang: superfun(langfreq) for lang, langfreq in db.iteritems()}

    smallest = _get_first(summed)
    for k, v in summed.iteritems():
        if v < smallest[1]:
            smallest = (k, v)
    return smallest


def _merge(db1, db2):
    pass

def train(text, lang, db):
    pass
    #return [lang, analyze(text)]

def guess(text, db):
    """Tries to guess the language of a given text"""
    return functclosest(analyze(text), db)


db = {'sv': analyze('okej nu blir det lite sveska i huset'),
        'en': analyze("okay well this is a little bit of english")
        }

freq = analyze("och nu har vi lite sveska att leka med igen")
