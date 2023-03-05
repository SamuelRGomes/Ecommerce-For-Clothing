from django.shortcuts import render , redirect

from django.contrib.auth.hashers import  check_password
from store.models.customer import Cliente
from django.views import  View
from store.models.product import Produto

class Cart(View):
    def get(self , request):
        data = {}
        ids = list(request.session.get('cart').keys())
        produtos = Produto.get_products_by_id(ids)  
        sizes = request.session.get('sizes')
        data['sizes'] = sizes
        data['produtos'] = produtos
        return render(request , 'cart.html' , data )
        #product_id = size for the product being selected and thrown into cart