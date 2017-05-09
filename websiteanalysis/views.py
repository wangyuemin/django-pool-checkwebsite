from django.shortcuts import render
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from . import selenium2
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
from . import takeurl
from django.http import StreamingHttpResponse
global ln
ln = []


async def foo(myqueue):
    while not myqueue.empty():
        selenium2.mainurl(myqueue.get())
        for this2plusurl in selenium2.linkurl:
            if not this2plusurl in f:
                f.add(this2plusurl)
                ln.append(this2plusurl)
                myqueue.put(this2plusurl)


def index(request):
    return render(request, 'index.html')


def add(request):
    a = request.POST['text']
    takeurl.takeurl(a)
    l = {}
    with open('/home/xuexiaobo/Downloads/python/selenium/urls.txt') as f:
        c = f.read()

    return render_to_response('output.html', {'username': c})


def download(request):
    # do something...

    def file_iterator(file_name, chunk_size=512):
        file_name = '/home/xuexiaobo/Downloads/python/selenium/urls.txt'
        with open(file_name) as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    the_file_name = "urls.txt"
    response = StreamingHttpResponse(file_iterator(the_file_name))
    response['Content-Type'] = 'application/octet-stream'
    response[
        'Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)

    return response
