from django.urls import re_path

from .views import cookiesetter

urlpatterns = [
    re_path(r'$', cookiesetter, name='cookiesetter'),
]