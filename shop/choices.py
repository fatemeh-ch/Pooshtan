from django.db import models


class ProductStatusType(models.IntegerChoices):
    """
    Defines the publication statuses of products.
    """

    PUBLISHED = (1, 'نمایش')
    DRAFT = (2, 'عدم نمایش')


class ProductSizeType(models.IntegerChoices):
    """
    Defines the available product size formats.
    """

    LETTER = (1, 'حروف')
    NUMERIC = (2, 'عدد')