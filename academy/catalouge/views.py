from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse
from catalouge.models import Product, Brand


def product_list(request):
    products = Product.objects.filter(Q(id__in=[1]) | Q(brand_id=4)).filter(product_type_id=1)
    # p1 = Brand(name= "bmw")
    # p1.name = "toyota"
    # p1.save()
    return HttpResponse("\n".join([f"{p.upc}" for p in products]))
