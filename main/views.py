from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def main(request):
    main_menu = MainMenu.objects.all()
    sub_menu = SubMenu.objects.all()
    sub_menu_katalog = SubMenu.objects.filter(main_menu=2)
    sub_menu_promo = SubMenu.objects.filter(main_menu=5)
    sub_category_menu = SubCategoryMenu.objects.all()
    products = Products.objects.all()
    settings = Settings.objects.all()
    page = 'glavnaya'
    return render(request, 'index.html', {'url': page, 'main_menu': main_menu, 'sub_menu': sub_menu, 'products': products, 'settings': settings, 'sub_category_menu': sub_category_menu, 'sub_menu_katalog': sub_menu_katalog, 'sub_menu_promo': sub_menu_promo})

def page(request, page):
    main_menu = MainMenu.objects.all()
    sub_menu = SubMenu.objects.all()
    sub_menu_katalog = SubMenu.objects.filter(main_menu=2)
    sub_menu_promo = SubMenu.objects.filter(main_menu=5)
    sub_category_menu = SubCategoryMenu.objects.all()
    products = Products.objects.all()
    settings = Settings.objects.all()
    return render(request, 'index.html', {'url': page, 'main_menu': main_menu, 'sub_menu': sub_menu, 'sub_category_menu': sub_category_menu, 'products': products, 'settings': settings, 'sub_menu_katalog': sub_menu_katalog, 'sub_menu_promo': sub_menu_promo})


def products(request, category, page):
    main_menu = MainMenu.objects.all()
    sub_menu = SubMenu.objects.all()
    sub_category_menu = SubCategoryMenu.objects.all()
    products = Products.objects.all()
    settings = Settings.objects.all()
    return render(request, 'products.html', {'url': page, 'main_menu': main_menu, 'sub_menu': sub_menu, 'products': products, 'settings': settings, 'sub_category_menu': sub_category_menu})
