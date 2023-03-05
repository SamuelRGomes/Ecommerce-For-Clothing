from django.db import models
from .category import Categoria
class Produto(models.Model):
    name = models.CharField(max_length=60)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Categoria,on_delete=models.CASCADE,default=1 )
    description = models.CharField(max_length=250, default='', blank=True, null= True)
    Tamanho_P = models.BooleanField(default=True)
    Tamanho_M = models.BooleanField(default=True)
    Tamanho_G = models.BooleanField(default=True)
    image= models.ImageField(upload_to='uploads/products/')

    @staticmethod
    def get_products_by_id(ids):
        return Produto.objects.filter (id__in=ids)
    @staticmethod
    def get_all_products():
        return Produto.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Produto.objects.filter (category=category_id)
        else:
            return Produto.get_all_products();