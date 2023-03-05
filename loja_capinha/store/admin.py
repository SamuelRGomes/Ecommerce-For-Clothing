from django.contrib import admin
from .models.product import Produto
from .models.category import Categoria
from .models.customer import Cliente
from .models.orders import Pedido


class AdminProduto(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['name']

# Register your models here.
admin.site.register(Produto,AdminProduto)
admin.site.register(Categoria)
admin.site.register(Cliente)
admin.site.register(Pedido)


