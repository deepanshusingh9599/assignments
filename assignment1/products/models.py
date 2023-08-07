from django.db import models

class Product(models.Model):
    '''Product Model'''
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()

    class Meta:
        db_table='product'
        ordering=['-id']
