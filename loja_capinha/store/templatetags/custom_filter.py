from django import template
import os
from loja_capinha import settings

register = template.Library()

@register.filter(name='currency')
def currency(number):
    return "R$ "+str(number)

@register.filter(name='multiply')
def multiply(number , number1):
    return number * number1

@register.filter
def env(key):
    return f'{settings.STATIC_URL}/{os.environ.get(key, None)}'
