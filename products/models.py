from django.db import models



class Product(models.Model):
    name = models.CharField(max_length=200)
    code = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='products/', height_field=None, width_field=None)

