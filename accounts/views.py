from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from accounts.forms import AuthenticationForm

# Create your views here.

class LoginView(auth_views.LoginView):

    form_class = AuthenticationForm
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True

    
    
class RegisterView(TemplateView):
    template_name = 'accounts/register.html'
