from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from store.models.customer import Cliente
from django.views import View

from store.models.product import Produto
from store.models.orders import Pedido


class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address') + ', ' + request.POST.get('complemento') + ', ' + request.POST.get('observacoes')
        request.session['address'] = address
        customer_id = request.session.get('customer')
        cliente = Cliente.get_customer_by_id(customer_id)
        phone = cliente.telefone
        email = cliente.email
        cart = request.session.get('cart')
        products = Produto.get_products_by_id(list(cart.keys()))
        sizes = list(request.session.get('sizes').values())

        for i in range(len(products)):
            order = Pedido(customer=Cliente(id=customer_id),
                          product=products[i],
                          price=products[i].price,
                          size = sizes[i],
                          address=address,
                          email = email,
                          phone=phone,
                          quantity=cart.get(str(products[i].id)))
            pedido = Pedido.get_all_orders()
            # order.save()
        request.session['cart'] = {}

        return render(request,'address.html')
