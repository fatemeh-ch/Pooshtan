from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import AuthenticationForm, UserCreationForm

# Create your views here.


class LoginView(auth_views.LoginView):
    """
    Handles user authentication for the Pooshtan website.

    Uses the custom authentication form and redirects
    authenticated users away from the login page.
    """

    form_class = AuthenticationForm
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True


class LogoutView(auth_views.LogoutView):
    """
    Handles user logout for the Pooshtan website.

    Uses Django's built-in LogoutView to terminate
    the user's authenticated session.
    """

    pass


class RegisterView(CreateView):
    """
    Handles new customer registration.

    Creates a customer account using the custom registration form
    and redirects the user to the login page after successful registration.
    """

    form_class = UserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')
