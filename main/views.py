from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.

def test(response):
    return render(response, 'main/extension.html')

def test_site(response):
    return render(response, 'main/test_sheet.html')





