from django.urls import path

from .views import *


urlpatterns = [
    path('',Product.as_view())
]
