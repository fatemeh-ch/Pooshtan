from django.conf import settings
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
    RegexValidator,
)

from django.db import models
from shop.choices import ProductStatusType,ProductSizeType


class ProductCategoryModel(models.Model):
    """
    Represents a category used to organize store products.

    Stores category information, its image, and activation status.
    """

    title = models.CharField(max_length=100,verbose_name='عنوان')

    slug = models.SlugField(
        max_length=200,
        unique=True,
        allow_unicode=True,
        verbose_name='اسلاگ'
    )

    image = models.ImageField(
        upload_to='shop/categories/',
        default='shop/categories/default-category.png',
        verbose_name='عکس'
    )

    is_active = models.BooleanField(default=False,verbose_name='فعال')

    created_at = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='تاریخ تغییر')

    class Meta:
        """
        Defines the default ordering of product categories.
        """

        ordering = ('title',)
        verbose_name = 'دسته‌بندی محصول'
        verbose_name_plural = 'دسته‌بندی محصولات'

    def __str__(self):
        """
        Returns the category title.
        """

        return self.title


class ProductModel(models.Model):
    """
    Represents a product available in the Pooshtan store.

    Stores product details, pricing, category, and publication status.
    """

    title = models.CharField(max_length=200,verbose_name='عنوان')

    slug = models.SlugField(
        max_length=200,
        unique=True,
        allow_unicode=True,
        verbose_name='اسلاگ'
    )

    brief_description = models.CharField(max_length=250,verbose_name='توضیح کوتاه')
    description = models.TextField(verbose_name='توضیحات کامل')

    category = models.ForeignKey(
        ProductCategoryModel,
        on_delete=models.PROTECT,
        related_name='products',
        verbose_name='دسته بندی'
    )

    price = models.DecimalField(
        max_digits=12,
        decimal_places=0,
        default=0,
        validators=[MinValueValidator(0)],
        verbose_name='قیمت'
    )

    discount_percent = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100),
        ],
        verbose_name='درصد تخفیف'
    )

    status = models.IntegerField(
        choices=ProductStatusType.choices,
        default=ProductStatusType.DRAFT.value,
        verbose_name='وضعیت'
    )

    created_at = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='تاریخ تغییر')

    class Meta:
        """
        Defines the default ordering of products.
        """

        ordering = ('-created_at',)
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        """
        Returns the product title.
        """

        return self.title


class ColorModel(models.Model):
    """
    Represents an available color for store products.
    """

    title = models.CharField(max_length=50,verbose_name='عنوان')

    slug = models.SlugField(
        max_length=70,
        unique=True,
        allow_unicode=True,
        verbose_name='اسلاگ'
    )

    hex_code = models.CharField(
        max_length=7,
        validators=[
            RegexValidator(
                regex=r'^#[0-9A-Fa-f]{6}$',
                message='فرمت کد رنگ معتبر نیست.',
            )
        ],
        verbose_name='کد هگزادسیمال'
    )

    created_at = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='تاریخ تغییر')

    class Meta:
        """
        Defines the default ordering of colors.
        """

        ordering = ('title',)
        verbose_name = 'رنگ'
        verbose_name_plural = 'رنگ‌ها'

    def __str__(self):
        """
        Returns the color title.
        """

        return self.title


class ProductColorModel(models.Model):
    """
    Represents a color assigned to a specific product.

    Connects products to their available colors.
    """

    product = models.ForeignKey(
        ProductModel,
        on_delete=models.CASCADE,
        related_name='product_colors',
        verbose_name='محصول'
    )

    color = models.ForeignKey(
        ColorModel,
        on_delete=models.PROTECT,
        related_name='product_colors',
        verbose_name='رنگ'
    )

    created_at = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='تاریخ تغییر')

    class Meta:
        """
        Defines uniqueness constraints for product colors.
        """

        constraints = [
            models.UniqueConstraint(
                fields=('product', 'color'),
                name='unique_product_color',
            )
        ]

        verbose_name = 'رنگ محصول'
        verbose_name_plural = 'رنگ‌های محصولات'

    def __str__(self):
        """
        Returns the product and its assigned color.
        """

        return f'{self.product.title} - {self.color.title}'


class ProductImageModel(models.Model):
    """
    Stores images associated with a product color.

    Allows each product color to have multiple images.
    """

    image = models.ImageField(
        upload_to='shop/products/',
        verbose_name='عکس'
    )

    alt_text = models.CharField(max_length=100,verbose_name='متن راهنما')

    product_color = models.ForeignKey(
        ProductColorModel,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='رنگ محصول'
    )

    created_at = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='تاریخ تغییر')

    class Meta:
        """
        Defines the default ordering of product images.
        """

        ordering = ('created_at',)
        verbose_name = 'تصویر محصول'
        verbose_name_plural = 'تصاویر محصولات'

    def __str__(self):
        """
        Returns the image file name.
        """

        return self.image.name


class ProductSizeModel(models.Model):
    """
    Represents an available size for store products.

    Supports both numeric and letter-based size formats.
    """

    title = models.CharField(max_length=10,verbose_name='عنوان')

    slug = models.SlugField(
        max_length=30,
        unique=True,
        allow_unicode=True,
        verbose_name='اسلاگ'
    )

    size_type = models.IntegerField(
        choices=ProductSizeType.choices,
        default=ProductSizeType.NUMERIC.value,
        verbose_name='نوع سایز'
    )

    created_at = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='تاریخ تغییر')

    class Meta:
        """
        Defines the default ordering of product sizes.
        """

        ordering = ('size_type', 'title')
        verbose_name = 'سایز'
        verbose_name_plural = 'سایزها'

    def __str__(self):
        """
        Returns the size title.
        """

        return self.title


class ProductVariantModel(models.Model):
    """
    Represents a specific product variant.

    Combines a product color and size and stores its stock quantity.
    """

    product_color = models.ForeignKey(
        ProductColorModel,
        on_delete=models.PROTECT,
        related_name='variants',
        verbose_name='رنگ محصول'
    )

    product_size = models.ForeignKey(
        ProductSizeModel,
        on_delete=models.PROTECT,
        related_name='variants',
        verbose_name='سایز محصول'
    )

    stock = models.PositiveIntegerField(default=0,verbose_name='موجودی')

    created_at = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='تاریخ تغییر')

    class Meta:
        """
        Defines uniqueness constraints for product variants.
        """

        constraints = [
            models.UniqueConstraint(
                fields=('product_color', 'product_size'),
                name='unique_product_color_size',
            )
        ]

        verbose_name = 'تنوع محصول'
        verbose_name_plural = 'تنوع محصولات'

    def __str__(self):
        """
        Returns the color and size of the product variant.
        """

        return (
            f'{self.product_color} - '
            f'{self.product_size.title}'
        )


class ProductComment(models.Model):
    """
    Stores customer comments submitted for products.

    Comments require administrator approval before publication.
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='product_comments',
        verbose_name='کاربر'
    )

    product = models.ForeignKey(
        ProductModel,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='محصول'
    )

    body = models.TextField(verbose_name='متن کامنت')

    is_approved = models.BooleanField(default=False,verbose_name='تایید شده')

    created_at = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='تاریخ تغییر')

    published_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='تاریخ انتشار'
    )

    class Meta:
        """
        Defines the default ordering of product comments.
        """

        ordering = ('-created_at',)
        verbose_name = 'نظر محصول'
        verbose_name_plural = 'نظرات محصولات'

    def __str__(self):
        """
        Returns the user email and associated product title.
        """

        return f'{self.user.email} - {self.product.title}'