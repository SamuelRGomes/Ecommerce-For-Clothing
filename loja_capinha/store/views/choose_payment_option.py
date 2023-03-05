from django.shortcuts import render , redirect , HttpResponseRedirect
from store.models.product import Produto
from store.models.category import Categoria
from django.views import View

def choose_payment_option():
    return render(request, 'index.html')