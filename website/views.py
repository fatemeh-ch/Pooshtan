from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from website.forms import ContactModelForm


# Create your views here.

class IndexView(TemplateView):
    template_name = 'website/index.html'


class AboutUsView(TemplateView):
    template_name = 'website/about-us.html'


class ContactUsView(CreateView):
    """
    Handles the submission of contact messages through the contact us page.

    Provides the contact form, pre-fills user information for authenticated
    users, and displays a success message after successful submission.
    """

    template_name = 'website/contact-us.html'
    form_class = ContactModelForm
    success_url = reverse_lazy('website:contact-us')

    def get_initial(self):
        """
        Returns the initial form data.

        Pre-fills the email address and full name fields with the
        authenticated user's information.
        """

        initial = super().get_initial()

        if self.request.user.is_authenticated:
            initial.update({
                'email': self.request.user.email,
                'user_full_name': (
                    f'{self.request.user.first_name} '
                    f'{self.request.user.last_name}'
                ).strip(),
            })

        return initial

    def form_valid(self, form):
        """
        Handles the form submission when the form is valid.

        Displays a success message and delegates the form processing
        to the parent CreateView.
        """

        messages.success(
            self.request,
            'پیام شما با موفقیت دریافت شد.'
        )
        return super().form_valid(form)