from django.shortcuts import render, get_object_or_404
from .cart import Cart  # Importa a classe Cart do arquivo cart.py
from store.models import Product  # Importa o modelo Product do aplicativo store
from django.http import JsonResponse  # Importa JsonResponse para retornar respostas JSON
from django.contrib import messages  # Importa messages para exibir mensagens de sucesso


def cart_summary(request):
    # Obtém o carrinho
    cart = Cart(request)
    cart_products = cart.get_prods  # Obtém os produtos do carrinho
    quantities = cart.get_quants  # Obtém as quantidades de cada produto
    totals = cart.cart_total()  # Calcula o total do carrinho
    return render(request, "cart_summary.html", {"cart_products": cart_products, "quantities": quantities, "totals": totals})


def cart_add(request):
    # Obtém o carrinho
    cart = Cart(request)
    # Verifica se a requisição é do tipo POST
    if request.POST.get('action') == 'post':
        # Obtém os dados do formulário
        product_id = int(request.POST.get('product_id'))  # ID do produto
        product_qty = int(request.POST.get('product_qty'))  # Quantidade do produto

        # Busca o produto no banco de dados
        product = get_object_or_404(Product, id=product_id)

        # Adiciona o produto ao carrinho com a quantidade especificada
        cart.add(product=product, quantity=product_qty)

        # Obtém a quantidade de itens no carrinho
        cart_quantity = cart.__len__()

        # Retorna uma resposta JSON com a quantidade atualizada no carrinho
        response = JsonResponse({'qty': cart_quantity})

        # Exibe uma mensagem de sucesso
        messages.success(request, ("Produto Adicionado ao Carrinho..."))
        return response


def cart_delete(request):
    cart = Cart(request)
    # Verifica se a requisição é do tipo POST
    if request.POST.get('action') == 'post':
        # Obtém os dados do formulário
        product_id = int(request.POST.get('product_id'))  # ID do produto

        # Chama o método delete do carrinho para remover o produto
        cart.delete(product=product_id)

        # Retorna uma resposta JSON informando que o produto foi removido
        response = JsonResponse({'product': product_id})

        # Exibe uma mensagem de sucesso
        messages.success(request, ("Produto Removido do Carrinho..."))
        return response


def cart_update(request):
    cart = Cart(request)
    # Verifica se a requisição é do tipo POST
    if request.POST.get('action') == 'post':
        # Obtém os dados do formulário
        product_id = int(request.POST.get('product_id'))  # ID do produto
        product_qty = int(request.POST.get('product_qty'))  # Nova quantidade do produto

        # Atualiza a quantidade do produto no carrinho
        cart.update(product=product_id, quantity=product_qty)

        # Retorna uma resposta JSON com a nova quantidade do produto
        response = JsonResponse({'qty': product_qty})

        # Exibe uma mensagem de sucesso
        messages.success(request, ("O Seu Carrinho foi Atualizado..."))
        return response
