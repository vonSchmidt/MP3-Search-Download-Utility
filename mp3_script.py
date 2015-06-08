#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mechanize
import re
from BeautifulSoup import BeautifulSoup
import downloader

def main():
    br = mechanize.Browser()
    query = "+".join(raw_input("Query Terms: > ").split(' '))
    response = br.open("http://mp3zap.com/?query=" + query)
    html = response.read().replace('"', "'")
    songs = BeautifulSoup(html).findAll('p')
    if not songs:
        print 'No Hits.'
        exit(0)
    songs = map(str, songs)
    songs = map(lambda e: e.replace('"', "'"), songs)
    offers = []
    for song in songs:
        match = re.findall("</a> <a rel='nofollow' href='(.+)' class='sm2_down'"\
                + " title='Download'></a><b>(.+)</b>(.+)</p>", song)
        if match:
            offers.append(match[0])
    for offer, i in zip(offers, range(len(offers))):
        print "\t\t".join(map(str, ((i + 1), offer[1], offer[2])))
    try:
        x = input('Choose: > ')
    except KeyboardInterrupt:
        print 'k bye.'
        exit(1)
    if (x <= 0 or x >= len(offers)):
        print 'Watch out!'
        exit(1)
    link = offers[x - 1][0]
    if not __import__('os').path.exists('./mp3/'):
        __import__('os').makedirs('./mp3/')
    downloader.download(link, './mp3/' + query.replace('+', '_') + '.mp3')

if __name__ == '__main__':
    try:
        main()
        exit(0)
    except KeyboardInterrupt, Exception:
        print 'Operation Cancelled.'
        exit(1)
