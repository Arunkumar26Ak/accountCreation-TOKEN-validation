from django.urls import path, include
from .user.views import createAccount
from .product.views import product
urlpatterns = [
    path('createAccount',createAccount),
    path('product',product),
]
