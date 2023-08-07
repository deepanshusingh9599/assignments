from django.db import models
from django.core import validators


class Movies(models.Model):
    '''Movies Model'''
    name = models.CharField(verbose_name='Movie Name', max_length=250)
    rating = models.IntegerField(validators=[validators.MaxValueValidator(5)], default=0)
    year = models.IntegerField(null= True)

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table='movies'
        ordering=['name']