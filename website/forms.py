from django import forms

from website.models import ContactModel


class ContactModelForm(forms.ModelForm):

    class Meta:
        model = ContactModel

        fields = ['subject', 'user_full_name', 'email', 'message']

        error_messages = {
            'subject': {
                'required': 'لطفاً موضوع پیام را وارد کنید.',
                'max_length': 'موضوع پیام بیش از حد طولانی است.',
            },

            'user_full_name': {
                'required': 'لطفاً نام و نام خانوادگی خود را وارد کنید.',
                'max_length': 'نام وارد شده بیش از حد طولانی است.',
            },

            'email': {
                'required': 'لطفاً ایمیل خود را وارد کنید.',
                'invalid': 'لطفاً یک آدرس ایمیل معتبر وارد کنید.',
            },

            'message': {
                'required': 'لطفاً متن پیام خود را وارد کنید.',
            },
        }

        labels = {
            'subject': 'موضوع پیام',
            'user_full_name': 'نام و نام خانوادگی',
            'email': 'ایمیل شما',
            'message': 'پیام شما',
        }

        widgets = {
            'user_full_name': forms.TextInput(attrs={
                'class': 'input-card',
                'placeholder': 'نام و نام خانوادگی *',
            }),

            'subject': forms.TextInput(attrs={
                'class': 'input-card',
                'placeholder': 'موضوع *',
            }),

            'email': forms.EmailInput(attrs={
                'class': 'input-card',
                'placeholder': 'ایمیل شما *',
            }),

            'message': forms.Textarea(attrs={
                'class': 'input-card',
                'placeholder': 'پیام شما *',
                'rows': 2,
            }),
        }
