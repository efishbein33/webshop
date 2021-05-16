from django.db import models


def string_representation(obj):
    '''given an object, returns the string representation of that object'''
    string = ''
    for key, value in obj.__dict__.items():
        if not key.startswith('_') and not key.startswith('__'):
            string += key + ': ' + str(value) + ', '
    string = string.rstrip(', ')
    return string


class Product(models.Model):
    name = models.CharField(max_length=200)
    code = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='products/', height_field=None, width_field=None)


    def __str__(self):
        return string_representation(self)