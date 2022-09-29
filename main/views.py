from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def test(response):
    return HttpResponse("<h3>Test</h3>")

def test2(response):
    return HttpResponse("<h3>Test2</h3>")

def test_site(response):
    return render(response, r'test_sheet.html')


