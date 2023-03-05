from django.contrib import admin
from django.urls import path
from . import views
from .views.home import Index , store
from .views.signup import Signup
from .views.login import Login , logout
from .views.cart import Cart
from .views.test2 import Test2
from .views.checkout import CheckOut
from .views.address import AddressView
from .views.create_checkout_session import create_checkout_session, success, cancel, checkout_payment
from .views.orders import OrderView
from .views.order_fulfillment import OrderFulfillmentView
from .views.orders_fulfilled import OrdersFulfilledView
from .views.payment import PaymentView
from .views.finalize import FinalizarWebScraper
from .middlewares.auth import auth_middleware


urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('store', store , name='store'),
    path('test2', Test2.as_view() , name='test2'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),    
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    path('create-checkout-session/', create_checkout_session, name='checkout'),
    path('success', success, name='success'),
    path('cancel', cancel, name='cancel'),
    path('checkout-payment', checkout_payment, name='cancel'),
    path('order-fulfillment', auth_middleware(OrderFulfillmentView.as_view()), name='order-fulfillment'),
    path('orders-fulfilled', auth_middleware(OrdersFulfilledView.as_view()), name='orders-fulfilled'),
    path('payment', auth_middleware(PaymentView.as_view()), name='payment'),
    path('finalizar', auth_middleware(FinalizarWebScraper.as_view()), name='finalize'),
    path('address', auth_middleware(AddressView.as_view()), name='address'),

]
