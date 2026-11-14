from django.db import models

# Create your models here.


class ContactModel(models.Model):
    """
    Represents a contact message submitted by a user through
    the contact us page.

    Stores the sender's information, message content, review status,
    and creation and update timestamps.
    """

    subject = models.CharField(max_length=255)
    user_full_name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    is_reviewed = models.BooleanField(default=False)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

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
