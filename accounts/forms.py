
from django import forms
from django.contrib.auth import forms as auth_forms
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext_lazy as _

from django.contrib.auth import get_user_model

from accounts.choices import UserType


User = get_user_model()


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
                'autocomplete': 'email',
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
                'autocomplete': 'current-password',
            }
        )
    )


class UserCreationForm(auth_forms.UserCreationForm):
    """
    Custom user registration form for Pooshtan.

    Registers customers using their email address and first name.
    Inherits password matching and password validation from
    Django's built-in UserCreationForm.
    """

    error_messages = {
        'password_mismatch': 'رمزهای عبور با یکدیگر مطابقت ندارند.',
    }

    email = forms.EmailField(
        label='ایمیل',
        error_messages={
            'required': 'وارد کردن ایمیل الزامی است.',
            'invalid': 'آدرس ایمیل معتبر نیست.',
        },
        widget=forms.EmailInput(
            attrs={
                'class': 'text-input',
                'placeholder': 'ایمیل',
                'autocomplete': 'email',
            }
        )
    )

    first_name = forms.CharField(
        label='نام',
        max_length=150,
        error_messages={
            'required': 'وارد کردن نام الزامی است.',
            'max_length': 'نام نمی‌تواند بیشتر از ۱۵۰ کاراکتر باشد.',
        },
        widget=forms.TextInput(
            attrs={
                'class': 'text-input',
                'placeholder': 'نام',
                'autocomplete': 'given-name',
            }
        )
    )

    password1 = forms.CharField(
        label='رمز عبور',
        strip=False,
        error_messages={
            'required': 'وارد کردن رمز عبور الزامی است.',
        },
        widget=forms.PasswordInput(
            attrs={
                'class': 'text-input',
                'placeholder': 'رمز عبور',
                'autocomplete': 'new-password',
            }
        )
    )

    password2 = forms.CharField(
        label='تکرار رمز عبور',
        strip=False,
        error_messages={
            'required': 'تکرار رمز عبور الزامی است.',
        },
        widget=forms.PasswordInput(
            attrs={
                'class': 'text-input',
                'placeholder': 'تکرار رمز عبور',
                'autocomplete': 'new-password',
            }
        )
    )

    class Meta:
        """
        Defines the User model and its registration fields.
        """

        model = User
        fields = ('email', 'first_name')

    def clean_email(self):
        """
        Validates the email address and checks for duplicates.

        Normalizes the email address before checking whether
        it is already registered.

        Raises:
            ValidationError: If the email is already in use.

        Returns:
            str: The normalized email address.
        """
        email = self.cleaned_data.get('email')

        email = User.objects.normalize_email(email)

        if User.objects.filter(email__iexact=email).exclude(
            pk=self.instance.pk
        ).exists():
            raise ValidationError(
                'این ایمیل قبلاً ثبت شده است.',
                code='unique',
            )

        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError('رمز عبور و تکرار آن یکسان نیستند.')

        errors = []

        try:
            validate_password(password2, self.instance)

        except ValidationError as e:

            for error in e.messages:

                if 'too short' in error:
                    errors.append('رمز عبور باید حداقل ۸ کاراکتر باشد.')

                elif 'too common' in error:
                    errors.append('رمز عبور انتخاب شده بسیار رایج است.')

                elif 'entirely numeric' in error:
                    errors.append('رمز عبور نباید فقط شامل اعداد باشد.')

                elif 'too similar' in error:
                    errors.append('رمز عبور نباید شبیه اطلاعات شخصی شما باشد.')

                else:
                    errors.append(error)

        if errors:
            raise ValidationError(errors)

        return password2

    def save(self, commit=True):
        """
        Creates a customer account with a securely hashed password.

        Assigns the CUSTOMER account type before saving the user,
        allowing the profile creation signal to identify the account.

        Args:
            commit: Whether to save the user immediately.

        Returns:
            User: The newly created user instance.
        """
        self.instance.user_type = UserType.CUSTOMER

        return super().save(commit=commit)
