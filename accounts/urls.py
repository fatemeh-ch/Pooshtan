from django.urls import path , include

from accounts.views import(
    LoginView,
    RegisterView
    
)

app_name='accounts'


urlpatterns = [
    path('login/',LoginView.as_view(),name='login'),
    path('register/',RegisterView.as_view(),name='register'),
    path('logout/',RegisterView.as_view(),name='logout'),
    path('dashboard/',RegisterView.as_view(),name='dashboard'),
]
