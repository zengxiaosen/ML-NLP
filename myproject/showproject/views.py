# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
def index(request):
    return render(request, 'index.html')
def provice(request):
    return render(request, 'provice.html')

def city(request):
    myjson = {
        'type': 'column',
        'colorByPoint': 'true',
        'data': [29.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4],
        'showInLegend': 'false'
    }
    data = json.dumps(myjson)
    return render(request, 'city.html', locals())

def hello(request):
    myjson = {
        'type': 'column',
        'colorByPoint': 'true',
        'data': [29.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4],
        'showInLegend': 'false'
    }
    data = json.dumps(myjson)
    return render(request, 'hello.html', locals())

