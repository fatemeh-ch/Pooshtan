from django.db import models

# Create your models here.


class ContactModel(models.Model):
    """
    Represents a contact message submitted by a user through
    the contact us page.

    Stores the sender's information, message content, review status,
    and creation and update timestamps.
    """

    subject = models.CharField(max_length=255,verbose_name='عنوان')
    user_full_name = models.CharField(max_length=255,verbose_name='نام کاربر')
    email = models.EmailField(verbose_name='ایمیل')
    message = models.TextField(verbose_name='بدنه پیام')

    is_reviewed = models.BooleanField(default=False,verbose_name='مشاهده شده')

    created_date = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ ایجاد')
    updated_date = models.DateTimeField(auto_now=True,verbose_name='تاریخ تغییر')

    class Meta:
        verbose_name='فرم تماس با ما'
        verbose_name_plural='فرم های تماس با ما'

    def __str__(self):
        """
        Returns a readable representation of the contact message.

        Includes the sender's full name and message subject.
        """
        return f'{self.user_full_name} - {self.subject}'


    def short_subject(self):
        """
        Returns a shortened version of the subject if it exceeds 25 characters.
        """

        if len(self.subject) > 25:
            return self.subject[:25] + '...'

        return self.subject
