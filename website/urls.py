from django.urls import path, include
from .views import (
    IndexView,
    AboutUsView,
    ContactUsView
)

app_name = 'website'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about-us/', AboutUsView.as_view(), name='about-us'),
    path('contact-us/', ContactUsView.as_view(), name='contact-us'),
]
