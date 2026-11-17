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


class LogoutView(auth_views.LogoutView):

    """
    Handles user logout for the Pooshtan website.

    Uses Django's built-in LogoutView to log out the user
    and redirect them to the homepage | index.
    """

    pass