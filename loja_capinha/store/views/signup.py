from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Cliente
from django.views import View


class Signup (View):
    def get(self, request):
        return render (request, 'signup.html')

    def post(self, request):
        postData = request.POST
        nome = postData.get('nome')
        sobrenome = postData.get('sobrenome')
        telefone = postData.get('telefone')
        email = postData.get('email')
        senha = postData.get('senha')
        value = {
            'nome': nome,
            'sobrenome': sobrenome,
            'telefone': telefone,
            'email': email
        }
        error_message = None

        customer = Cliente (nome=nome,
                             sobrenome=sobrenome,
                             telefone=telefone,
                             email=email,
                             senha=senha)
        print(customer)
        error_message = self.validateCustomer(customer)

        if not error_message:
            customer.senha = make_password(customer.senha)
            customer.register()
            request.session['customer'] = customer.id
            request.session['email'] = customer.email
            return redirect ('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render (request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_message = None
        if (not customer.nome):
            error_message = "Por favor, Insira seu nome"
        elif len (customer.nome) < 3:
            error_message = 'Nome deve ter mais de 3 caracteres'
        elif not customer.sobrenome:
            error_message = 'Por favor, Insira seu sobrenome'
        elif len (customer.sobrenome) < 3:
            error_message = 'Sobrenome deve ter mais de 3 caracteres'
        elif not customer.telefone:
            error_message = 'Insira seu número de telefone'
        elif len (customer.telefone) < 10:
            error_message = 'Telefone deve ter mais de 10 caracteres'
        elif len (customer.senha) < 5:
            error_message = 'Senha deve ter mais de 5 caracteres'
        elif len (customer.email) < 5:
            error_message = 'Email deve ter mais de 5 caracteres'
        elif customer.isExists ():
            error_message = 'Endereço de email já registrado'
        # saving

        return error_message
