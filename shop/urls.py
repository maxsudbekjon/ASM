from django.urls import path

from shop.views import CategoryListView, ProductListView

urlpatterns=[
    path('category',CategoryListView.as_view(),name='shop_list'),
    path('product-detail',ProductListView.as_view(),name='shop_list')
]