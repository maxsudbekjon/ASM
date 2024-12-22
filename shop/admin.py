from django.contrib import admin

from shop.models import Category,Product,ProductImage,Color,Size

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Size)
admin.site.register(Color)