from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from website.forms import ContactModelForm
from shop.models import ProductCategoryModel, ProductModel
from shop.choices import ProductStatusType


# Create your views here.


class IndexView(TemplateView):
    """Display the website homepage with active categories and published products."""

    template_name = 'website/index.html'

    def get_context_data(self, **kwargs):
        """Add active categories and published products to the template context."""
        context = super().get_context_data(**kwargs)

        context['categories'] = ProductCategoryModel.objects.filter(
            is_active=True
        )

        context['products'] = ProductModel.objects.filter(
            status=ProductStatusType.PUBLISHED
        ).prefetch_related(
            'product_colors__images'
        )

        return context



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
