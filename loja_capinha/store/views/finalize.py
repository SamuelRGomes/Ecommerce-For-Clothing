from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from store.models.customer import Cliente
from django.views import View

from store.models.product import Produto
from store.models.orders import Pedido
import requests
import lxml
from bs4 import BeautifulSoup as bs
class FinalizarWebScraper (View):
    def get(self, request):
        return render(request,'finalizando.html')
    def post(self, request):
        cepDestino = request.POST.get('cep')
        url = f'http://ws.correios.com.br/calculador/CalcPrecoPrazo.aspx?sCepOrigem=01010904&sCepDestino={cepDestino}&nVlPeso=0.3&nCdFormato=1&nVlComprimento=20&nVlAltura=20&nVlLargura=20&nVlDiametro=0&nCdServico=04014&nCdEmpresa=&sDsSenha=&sCdMaoPropria=n&nVlValorDeclarado=0&sCdAvisoRecebimento=n&StrRetorno=xml&nIndicaCalculo=3'
        data = requests.get(url)
        bs_content = bs(data.text,"xml")
        frete = bs_content.find("Valor").get_text()
        frete = frete.replace(",",".")
        street = request.POST.get('street')
        number = request.POST.get('number')
        complement = request.POST.get('complement')
        neighborhood = request.POST.get('neighborhood')
        city = request.POST.get('city')
        region = request.POST.get('region')
        cart = request.session.get('cart')
        products = Produto.get_products_by_id(list(cart.keys()))
        info = {'frete':frete,'cepDestino':cepDestino,'street':street, 'number':number, 'complement':complement,'neighborhood':neighborhood,'city':city,'region':region, 'products':products}
        customer_id = request.session.get('customer')
        cliente = Cliente.get_customer_by_id(customer_id)
        phone = cliente.telefone
        email = cliente.email
        cart = request.session.get('cart')
        products = Produto.get_products_by_id(list(cart.keys()))
        sizes = list(request.session.get('sizes').values())
        info['cart'] = cart
        cliente_nome = cliente.nome
        info['cliente_nome'] = cliente_nome
        info['cliente_email'] = email
        info['cliente_phone'] = phone[2:]
        info['cliente_areacode'] = phone[:2]
        print(info)
        stuff = "hello"
        for i in range(len(products)):
            order = Pedido(customer=Cliente(id=customer_id),
                          product=products[i],
                          price=products[i].price,
                          size = sizes[i],
                          address=street,
                          email = email,
                          phone=phone,
                          quantity=cart.get(str(products[i].id)))
            order.save()
            request.session['cart'] = {}
        return render(request,'finalizando.html',info)