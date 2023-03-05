from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Cliente
from django.views import View


class Test2 (View):
    def get(self, request):
        return render (request, 'test2.html')