from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Cliente
from django.views import View
from store.models.product import Produto
from store.models.orders import Pedido
from store.middlewares.auth import auth_middleware

class PaymentView(View):
    def get(self , request ):
        cart = request.session.get('cart')
        cart = {}
        request.session['cart'] = cart
        return render(request , 'payment.html')