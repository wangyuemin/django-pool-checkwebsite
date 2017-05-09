from.import selenium2
from multiprocessing import Pool
import re
import os
from selenium import webdriver
import queue
import time
import multiprocessing
from pybloom import BloomFilter
import asyncio
from asyncio import Queue


def takeurl(takurl, regip):
    ln = []
    f = BloomFilter(capacity=100000, error_rate=0.001)
    myqueue = queue.Queue()
    url = takurl
    f.add(url)
    ln.append(url)
    selenium2.mainurl(url)
    for this2plusurl in selenium2.linkurl:
        if not this2plusurl in f:
            f.add(this2plusurl)
            ln.append(this2plusurl)
            myqueue.put(this2plusurl)
    print (myqueue.qsize())
    while not myqueue.empty():
        selenium2.mainurl(myqueue.get())
        for this2plusurl in selenium2.linkurl:
            if not this2plusurl in f:
                f.add(this2plusurl)
                ln.append(this2plusurl)
                myqueue.put(this2plusurl)
    print (len(ln))
    print (ln)
    print (myqueue.qsize())
    f = open('/home/xuexiaobo/Downloads/python/selenium/%s.txt' % (regip), 'a')
    for i in ln:
        f.write(str(i) + '\n')
    f.close
