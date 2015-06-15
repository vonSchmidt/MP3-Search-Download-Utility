#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2

referer = 'http://mp3zap.com/'

def download(url, filename):
    request = urllib2.Request(url)
    request.add_header('Referer', referer)
    response = urllib2.urlopen(request)
    f = open(filename, "wb")
    meta = response.info()
    filesize = int(meta.getheaders("Content-Length")[0])
    print "Downloading %s Bytes -- Output File: %s" % (filesize, filename)

    file_size_dl = 0
    blocks_sz = 8192
    while 1:
        buffer = response.read(8192)
        if not buffer:
            break
        file_size_dl += len(buffer)
        f.write(buffer)
        status = r"   ===  [ Downloaded: %15d ] [%3.1f%%] [ File Size: %15d ]  ===   " % (file_size_dl, file_size_dl * 100 / filesize, filesize)
        print status + "\r",
    f.close()
