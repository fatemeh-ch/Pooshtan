from django.db import models

# Create your models here.


class ContactModel(models.Model):

# A class fo?r 
    subject = models.CharField(max_length=255)
    user_full_name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    is_reviewed=models.BooleanField(default=False)

    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f' {self.user_full_name} - {self.subject}'