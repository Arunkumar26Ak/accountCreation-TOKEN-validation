from django.urls import path, include
from .views import signin
urlpatterns = [
    path('signin', signin),
    path('proj/signin', signin),
    path('',include('apps.proj.urls')),
]