from django.contrib import admin
from .models import Category, Customer, Product, Order, Profile
from django.contrib.auth.models import User

# Registrar os modelos no painel de administração do Django
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Profile)


# Misturar informações do perfil e informações do usuário
class ProfileInline(admin.StackedInline):
    model = Profile

# Estender o modelo de Usuário
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username", "first_name", "last_name", "email"]
    inlines = [ProfileInline]

# Cancelar o registro do modelo de Usuário da forma antiga
admin.site.unregister(User)

# Registrar novamente de forma personalizada
admin.site.register(User, UserAdmin)
