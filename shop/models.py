from django.db import models


class Category(models.Model):
    image = models.ImageField(upload_to='category/%Y')
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Size(models.Model):
    size = models.CharField(max_length=5)  # XS, S, M, L kabi o'lchamlar

    def __str__(self):
        return self.size


class Color(models.Model):
    color = models.CharField(max_length=255)  # Rang nomi, masalan, "Red"

    def __str__(self):
        return self.color


class ProductImage(models.Model):
    product = models.ForeignKey(
        'Product', on_delete=models.CASCADE, related_name='images'
    )
    image = models.ImageField(upload_to='product/image/%Y/%m/%d')

    def __str__(self):
        return f"Image for {self.product.title}"


class Product(models.Model):
    title = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=20, decimal_places=1)
    description = models.TextField()
    sizes = models.ManyToManyField(Size, related_name='products')  # Many-to-Many field
    colors = models.ManyToManyField(Color, related_name='products')  # Many-to-Many field
    promotions = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.IntegerField()
    specification = models.CharField(max_length=255, blank=True, null=True)
    reviews = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title
