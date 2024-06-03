import datetime
from django.contrib.auth.models import User
from django.test import TestCase
from .models import Profile, Category, Customer, Product, Order

class ModelTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create(username='testuser')

    def test_profile_creation(self):
        # Test profile creation when a user is created
        profile = Profile.objects.get(user=self.user)
        self.assertIsNotNone(profile)
        self.assertEqual(profile.user, self.user)

    def test_category_creation(self):
        # Test category creation
        category = Category.objects.create(name='Test Category')
        self.assertIsNotNone(category)
        self.assertEqual(category.name, 'Test Category')

    def test_customer_creation(self):
        # Test customer creation
        customer = Customer.objects.create(first_name='John', last_name='Doe', phone='1234567890', email='test@example.com', password='password')
        self.assertIsNotNone(customer)
        self.assertEqual(customer.first_name, 'John')
        self.assertEqual(customer.last_name, 'Doe')

    def test_product_creation(self):
        # Test product creation
        category = Category.objects.create(name='Test Category')
        product = Product.objects.create(name='Test Product', price=10.00, category=category)
        self.assertIsNotNone(product)
        self.assertEqual(product.name, 'Test Product')
        self.assertEqual(product.price, 10.00)

    def test_order_creation(self):
        # Test order creation
        category = Category.objects.create(name='Test Category')
        product = Product.objects.create(name='Test Product', price=10.00, category=category)
        customer = Customer.objects.create(first_name='John', last_name='Doe', phone='1234567890', email='test@example.com', password='password')
        order = Order.objects.create(product=product, customer=customer, quantity=1, address='123 Test St', phone='1234567890', date=datetime.date.today(), status=False)
        self.assertIsNotNone(order)
        self.assertEqual(order.product, product)
        self.assertEqual(order.customer, customer)
