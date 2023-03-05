from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Cliente
from django.views import View
from store.models.product import Produto
from store.models.orders import Pedido
from store.middlewares.auth import auth_middleware

class OrderView(View):

    def get(self , request ):
        customer = request.session.get('customer')
        orders = Pedido.get_orders_by_customer(customer)
        return render(request , 'orders.html'  , {'orders' : orders})
