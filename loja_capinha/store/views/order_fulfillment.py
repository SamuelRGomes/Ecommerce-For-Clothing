from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Cliente
from django.views import View
from store.models.product import Produto
from store.models.orders import Pedido
from store.middlewares.auth import auth_middleware

class OrderFulfillmentView(View):
    def get(self , request ):
        customer = request.session.get('customer')
        orders = Pedido.get_all_orders()
        return render(request , 'order_fulfillment.html'  , {'orders' : orders})
    def post(self , request):
        order_id = request.POST.get('order_id')
        order = Pedido.get_order_by_id(order_id)
        Pedido.toggle_status(order[0])
        return redirect('/order-fulfillment')