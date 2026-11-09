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
    template_name = 'website/contact-us.html'
    form_class = ContactModelForm
    success_url = reverse_lazy('website:contact-us')

    def form_valid(self, form):
        messages.success(
            self.request,
            'پیام شما با موفقیت دریافت شد.'
        )
        return super().form_valid(form)
