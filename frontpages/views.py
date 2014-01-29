# Create your views here.
from django.shortcuts import render, redirect
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib import messages


def home(request):
    context = {}
    return render(request,
                  "frontpages/home.html",
                  context)


def about(request):
    context = {}
    return render(request,
                  "frontpages/about.html",
                  context)


def contact(request):
    context = {}
    return render(request,
                  "frontpages/contact.html",
                  context)
