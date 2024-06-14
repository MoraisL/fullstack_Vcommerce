import datetime
from django.contrib.auth.models import User
from django.test import TestCase
from .models import Profile, Category, Customer, Product, Order

class ModelTestCase(TestCase):
    def setUp(self):
        # Criar um usuário de teste
        self.user = User.objects.create(username='testuser')

    def test_profile_creation(self):
        # Testar a criação do perfil quando um usuário é criado
        profile = Profile.objects.get(user=self.user)
        self.assertIsNotNone(profile)
        self.assertEqual(profile.user, self.user)

    def test_category_creation(self):
        # Testar a criação de categoria
        category = Category.objects.create(name='Categoria de Teste')
        self.assertIsNotNone(category)
        self.assertEqual(category.name, 'Categoria de Teste')

    def test_customer_creation(self):
        # Testar a criação de cliente
        customer = Customer.objects.create(first_name='João', last_name='Silva', phone='1234567890', email='teste@example.com', password='senha')
        self.assertIsNotNone(customer)
        self.assertEqual(customer.first_name, 'João')
        self.assertEqual(customer.last_name, 'Silva')

    def test_product_creation(self):
        # Testar a criação de produto
        category = Category.objects.create(name='Categoria de Teste')
        product = Product.objects.create(name='Produto de Teste', price=10.00, category=category)
        self.assertIsNotNone(product)
        self.assertEqual(product.name, 'Produto de Teste')
        self.assertEqual(product.price, 10.00)

    def test_order_creation(self):
        # Testar a criação de pedido
        category = Category.objects.create(name='Categoria de Teste')
        product = Product.objects.create(name='Produto de Teste', price=10.00, category=category)
        customer = Customer.objects.create(first_name='João', last_name='Silva', phone='1234567890', email='teste@example.com', password='senha')
        order = Order.objects.create(product=product, customer=customer, quantity=1, address='Rua Teste, 123', phone='1234567890', date=datetime.date.today(), status=False)
        self.assertIsNotNone(order)
        self.assertEqual(order.product, product)
        self.assertEqual(order.customer, customer)
