from django.shortcuts import render , redirect , HttpResponseRedirect
from store.models.product import Produto
from store.models.category import Categoria
from django.views import View


# Create your views here.
class Index(View):

    def post(self , request):
        size = request.session.get('size')
        produto = request.POST.get('produto')
        remove = request.POST.get('remove')
        url = request.POST.get('url')
        cart = request.session.get('cart')        
        sizes = request.session.get('sizes')
        produto_queryset = Produto.get_products_by_id(produto)
        if not sizes.get(produto) and not remove:
            sizes[produto] = size
        if sizes.get(produto) and remove:
            sizes.pop(produto)
        if cart:
            quantity = cart.get(produto)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(produto)   
                    else:
                        cart[produto]  = quantity-1
                else:
                    cart[produto]  = quantity+1

            else:
                cart[produto] = 1
        else:
            cart = {}
            cart[produto] = 1
        request.session['sizes'] = sizes
        request.session['cart'] = cart
        request.session['size'] = None
        return redirect(url)



    def get(self , request):
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')

def store(request):
    if request.session.get("email"):
        if request.session.get('email') == 'administrador@admin.com':
            return redirect ('order-fulfillment')
    sizes = request.session.get('sizes')
    if not sizes:
        request.session['sizes'] = {}
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    produtos = None
    categorias = Categoria.get_all_categories()
    size = request.GET.get('size')
    if not size:
         size = request.session.get('size')
    request.session['size'] = size
    categoryID = request.GET.get('categoria')
    if categoryID:
        produtos = Produto.get_all_products_by_categoryid(categoryID)
    else:
        produtos = Produto.get_all_products()

    data = {}
    data['produtos'] = produtos
    data['categorias'] = categorias
    data['size'] = size
    print('you are : ', request.session.get('email'))
    return render(request, 'index.html', data)


