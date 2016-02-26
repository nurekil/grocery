# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from django.contrib import admin
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from main.models import Category, Item


def index(request):
    categories = Category.objects.all()

    context = {'categories': categories}

    return render(request, 'index.html', context)

def cart(request):
    items = Item.objects.all()
    categories = Category.objects.all()

    context = {'items': items, 'categories': categories}

    return render(request, 'cart.html', context)


def item_about(request, alias):
    try:
        item = Item.objects.get(alias=alias)
    except:
        return Http404
    
    categories = Category.objects.all()

    context = {'item': item, 'categories': categories}

    return render(request, 'item_about.html', context)


def category_items(request, alias):
    try:
        category = Category.objects.get(alias=alias)
        items = Item.objects.filter(category=category)
    except:
        return Http404

    categories = Category.objects.all()

    context = {'items': items, 'category': category, 'categories': categories}

    return render(request, 'items.html', context)

def order(request):

    return render_to_response('index', [])
