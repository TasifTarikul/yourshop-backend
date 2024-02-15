from rest_framework.test import APIRequestFactory, APITestCase

from project_root.product.models import Product, Category
from .views import ProductView

class ProductAPITest(APITestCase):

    def setUp(self):
        c = Category.objects.create(title='Electronics')
        Product.objects.create(title='Test Product 1', category=c)
        Product.objects.create(title='Test Product 2', category=c)

    def test_get_all_product(self):
        factory = APIRequestFactory()
        view = ProductView.as_view({'get': 'list'})
        request = factory.get('/api/v1/product/admin/product/admin-product')
        response = view(request)
        assert response.status_code == 200


        