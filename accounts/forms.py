
from django import forms
from django.contrib.auth import forms as auth_forms


class AuthenticationForm(auth_forms.AuthenticationForm):
    """
    Custom authentication form for Pooshtan.

    Uses email as the login identifier and customizes
    field widgets and validation error messages.
    """

    error_messages = {
        'invalid_login': 'ایمیل یا رمز عبور وارد شده صحیح نیست.',
        'inactive': 'این حساب کاربری غیرفعال است.',
    }

    username = forms.EmailField(
        label='ایمیل',
        error_messages={
            'required': 'وارد کردن ایمیل الزامی است.',
            'invalid': 'فرمت ایمیل وارد شده معتبر نیست.',
        },
        widget=forms.EmailInput(
            attrs={
                'class': 'text-input',
                'placeholder': 'ایمیل',
                'autocomplete': 'off',
            }
        )
    )

    password = forms.CharField(
        label='رمز عبور',
        strip=False,
        error_messages={
            'required': 'وارد کردن رمز عبور الزامی است.',
        },
        widget=forms.PasswordInput(
            attrs={
                'class': 'text-input',
                'placeholder': 'رمز عبور',
                'autocomplete': 'off',
            }
        )
    )
