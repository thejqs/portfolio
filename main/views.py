import os, sys
from django.shortcuts import render
from django.conf import settings

sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")


def thejqs(request):
    return render(request, 'thejqs.html')


def portfolio(request):
    return render(request, 'portfolio.html')


def about(request):
    return render(request, 'about.html')
