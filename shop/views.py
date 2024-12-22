# Create your views here.
from django.shortcuts import render
from django.views import View

from shop.models import Category, Product


class CategoryListView(View):

    def get(self,request):
        data=Category.objects.all()
        context={
            'context':data
        }
        return render(request,'shop/shop.html',context=context)
class ProductListView(View):

    def get(self,request):
        data=Product.objects.all()
        context={
            'context':data
        }
        return render(request,'shop/product-details.html',context=context)
