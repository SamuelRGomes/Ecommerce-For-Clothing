import environ
env = environ.Env()
environ.Env.read_env()
import stripe
from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt

stripe.api_key = env('STRIPE_PRIVATE_KEY')
YOUR_DOMAIN = 'http://127.0.0.1:8000'

@csrf_exempt
def create_checkout_session(request):
 session = stripe.checkout.Session.create(
 payment_method_types=['card'],
 line_items=[{
 'price_data': {
 'currency': 'inr',
 'product_data': {
 'name': 'Intro to Django Course',
 },
 'unit_amount': 10000,
 },
 'quantity': 1,
 }],
 mode='payment',
 success_url=YOUR_DOMAIN + '/success.html',
 cancel_url=YOUR_DOMAIN + '/cancel.html',
 )
 return JsonResponse({'id': session.id})


def success(request):
    return render(request,'success.html')

def cancel(request):
    return render(request,'cancel.html')

def checkout_payment(request):
    return render(request,'checkout_payment.html')