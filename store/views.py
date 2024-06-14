from django.shortcuts import render, redirect
from .models import Product, Category, Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .serializers import CategorySerializer, ProductSerializer, ProfileSerializer, CustomerSerializer, OrderSerializer
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, UpdateUserForm, ChangePasswordForm, UserInfoForm
from django import forms
from django.db.models import Q


def search(request):
    # Verifica se o formulário foi preenchido
    if request.method == "POST":
        searched = request.POST['searched']
        # Consulta o modelo de produtos (Product)
        searched = Product.objects.filter(Q(name__icontains=searched) | Q(description__icontains=searched))
        # Verifica se não há resultados
        if not searched:
            messages.success(request, "Este Produto Não Existe, por favor Tente Novamente...")
            return render(request, "search.html", {})
        else:
            return render(request, "search.html", {'searched': searched})
    else:
        return render(request, "search.html", {})	
	

def update_info(request):
    if request.user.is_authenticated:
        current_user = Profile.objects.get(user__id=request.user.id)
        form = UserInfoForm(request.POST or None, instance=current_user)

        if form.is_valid():
            form.save()
            messages.success(request, "Suas informações foram atualizadas com sucesso!!")
            return redirect('home')
        return render(request, "update_info.html", {'form': form})
    else:
        messages.success(request, "Você deve estar logado para acessar essa página!!")
        return redirect('home')


def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user
        # Verifica se o formulário foi preenchido
        if request.method == 'POST':
            form = ChangePasswordForm(current_user, request.POST)
            # Verifica se o formulário é válido
            if form.is_valid():
                form.save()
                messages.success(request, "A Senha Foi Atualizada...")
                login(request, current_user)
                return redirect('update_user')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
                return redirect('update_password')
        else:
            form = ChangePasswordForm(current_user)
            return render(request, "update_password.html", {'form': form})
    else:
        messages.success(request, "Você deve estar logado para acessar essa página...")
        return redirect('home')


def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.POST or None, instance=current_user)

        if user_form.is_valid():
            user_form.save()

            login(request, current_user)
            messages.success(request, "O usuário foi atualizado!!")
            return redirect('home')
        return render(request, "update_user.html", {'user_form': user_form})
    else:
        messages.success(request, "Você deve estar logado para acessar essa página!!")
        return redirect('home')


def category_summary(request):
    categories = Category.objects.all()
    return render(request, 'category_summary.html', {"categories": categories})	


def category(request, foo):
    # Substitui hifens por espaços
    foo = foo.replace('-', ' ')
    # Obtém a categoria da URL
    try:
        # Busca a categoria
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'products': products, 'category': category})
    except:
        messages.success(request, ("Esta Categoria Não Existe..."))
        return redirect('home')


def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product': product})


def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


def about(request):
    return render(request, 'about.html', {})	


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("Você já está na sua conta!"))
            return redirect('home')
        else:
            messages.success(request, ("Ocorreu um erro com as suas credenciais, tente novamente..."))
            return redirect('login')

    else:
        return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, ("Você foi desconectado... Obrigado por passar por aqui..."))
    return redirect('home')


def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # Faz o login do usuário
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Username criado - Preencha suas informações de usuário abaixo..."))
            return redirect('update_info')
        else:
            messages.success(request, ("Houve um problema ao registrar, por favor tente novamente..."))
            return redirect('register')
    else:
        return render(request, 'register.html', {'form': form})
