from django.db import models
import uuid
import enum

# Create your models here.


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(verbose_name='Name', max_length=50)
    description = models.TextField(verbose_name='Desc', max_length=200)
    
    class TYPE:
        MOBILE = 'Mob'
        LAPTOP = 'Lap'

    TYPE_CHOICES = (
        (TYPE.MOBILE, 'MOBILE'),
        (TYPE.LAPTOP, 'LAPTOP'),
    )
    type = models.CharField(max_length=15, choices=TYPE_CHOICES)

    def __str__(self):
        return '{}'.format(self.name)

    @property
    def product_attribute(self):
        return self.productattribute_set.all()


   


class ProductAttribute(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    processor = models.CharField(max_length=50)
    ram =  models.CharField(max_length=20)
    screen_size = models.CharField(blank=True,max_length=20)
    colour = models.CharField(blank=True,max_length=20)
    hd_capacity = models.CharField(blank=True,max_length=20)


    def __str__(self):
        return '{}'.format(self.id)


