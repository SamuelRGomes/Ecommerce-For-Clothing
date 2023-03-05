from django.db import models
from .product import Produto
from .customer import Cliente
import datetime


class Pedido(models.Model):
    product = models.ForeignKey(Produto,
                                on_delete=models.CASCADE)
    customer = models.ForeignKey(Cliente,
                                 on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    size = models.CharField (max_length=50, default='P', blank=True)
    email = models.EmailField(null=True)
    address = models.CharField (max_length=150, default='')
    phone = models.CharField (max_length=50, default='', blank=True)
    date = models.DateField (default=datetime.datetime.today)
    status = models.BooleanField (default=False)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Pedido.objects.filter(customer=customer_id).order_by('-date')

    @staticmethod
    def get_order_by_id(id):
        return Pedido.objects.filter(id=id)

    @staticmethod
    def toggle_status(order):
        order.status = not order.status
        order.save()

    @staticmethod
    def get_all_orders():
        return Pedido.objects.all()

