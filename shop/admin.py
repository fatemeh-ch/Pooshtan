
from django.contrib import admin
from django.utils import timezone

from shop.models import (
    ProductModel,
    ProductCategoryModel,
    ProductColorModel,
    ProductImageModel,
    ProductComment,
    ProductVariantModel,
    ProductSizeModel,
    ColorModel,
)


@admin.register(ProductModel)
class CustomProductAdmin(admin.ModelAdmin):
    """Configures the Django admin interface for products."""

    prepopulated_fields = {
        'slug': ('title',)
    }

    list_display = [
        'title',
        'category',
        'price',
        'discount_percent',
        'status',
        'created_at',
    ]

    fields = [
        'title',
        'slug',
        ('brief_description', 'description'),
        'category',
        'price',
        'discount_percent',
        'status',
        'created_at',
        'updated_at',
    ]

    list_filter = [
        'status',
        'category',
        'created_at',
    ]

    ordering = ['-created_at']

    search_fields = [
        'title',
        'slug',
        'description',
        'category__title',
    ]

    readonly_fields = [
        'created_at',
        'updated_at',
    ]

    list_select_related = ['category']

    empty_value_display = 'خالی'


@admin.register(ProductCategoryModel)
class CustomProductCategoryAdmin(admin.ModelAdmin):
    """Configures the Django admin interface for product categories."""

    prepopulated_fields = {
        'slug': ('title',)
    }

    list_display = [
        'title',
        'slug',
        'is_active',
        'alt_text',
        'created_at',
    ]

    fields = [
        ('title', 'slug'),
        'alt_text',
        'is_active',
        'image',
        'created_at',
        'updated_at',
    ]

    list_filter = [
        'is_active',
        'created_at',
    ]

    ordering = ['-created_at']

    search_fields = [
        'title',
        'slug',
    ]

    readonly_fields = [
        'created_at',
        'updated_at',
    ]

    empty_value_display = 'خالی'


@admin.register(ProductColorModel)
class CustomProductColorAdmin(admin.ModelAdmin):
    """Configures the Django admin interface for product colors."""

    list_display = [
        'product',
        'color',
        'created_at',
    ]

    fields = [
        'product',
        'color',
        'created_at',
        'updated_at',
    ]

    ordering = ['-created_at']

    search_fields = [
        'product__title',
        'color__title',
    ]

    readonly_fields = [
        'created_at',
        'updated_at',
    ]

    list_select_related = [
        'product',
        'color',
    ]

    empty_value_display = 'خالی'


@admin.register(ProductImageModel)
class CustomProductImageAdmin(admin.ModelAdmin):
    """Configures the Django admin interface for product images."""

    list_display = [
        'image',
        'product_color',
        'alt_text',
        'created_at',
    ]

    fields = [
        'image',
        'product_color',
        'alt_text',
        'created_at',
        'updated_at',
    ]

    list_filter = [
        'product_color__color',
        'created_at',
    ]

    ordering = ['-created_at']

    search_fields = [
        'product_color__product__title',
        'product_color__color__title',
        'alt_text',
    ]

    readonly_fields = [
        'created_at',
        'updated_at',
    ]

    list_select_related = [
        'product_color',
        'product_color__product',
        'product_color__color',
    ]

    empty_value_display = 'خالی'


@admin.register(ColorModel)
class CustomColorAdmin(admin.ModelAdmin):
    """Configures the Django admin interface for available colors."""

    prepopulated_fields = {
        'slug': ('title',)
    }

    list_display = [
        'title',
        'slug',
        'hex_code',
        'created_at',
    ]

    fields = [
        ('title', 'slug'),
        'hex_code',
        'created_at',
        'updated_at',
    ]

    ordering = ['title']

    search_fields = [
        'title',
        'slug',
        'hex_code',
    ]

    readonly_fields = [
        'created_at',
        'updated_at',
    ]

    empty_value_display = 'خالی'


@admin.register(ProductSizeModel)
class CustomProductSizeAdmin(admin.ModelAdmin):
    """Configures the Django admin interface for product sizes."""

    prepopulated_fields = {
        'slug': ('title',)
    }

    list_display = [
        'title',
        'slug',
        'size_type',
    ]

    fields = [
        'title',
        'slug',
        'size_type',
        'created_at',
        'updated_at',
    ]

    list_filter = [
        'size_type',
    ]

    ordering = [
        'size_type',
        'title',
    ]

    search_fields = [
        'title',
        'slug',
    ]

    readonly_fields = [
        'created_at',
        'updated_at',
    ]

    empty_value_display = 'خالی'


@admin.register(ProductVariantModel)
class CustomProductVariantAdmin(admin.ModelAdmin):
    """Configures the Django admin interface for product variants."""

    list_display = [
        'product_color',
        'product_size',
        'stock',
        'created_at',
    ]

    fields = [
        'product_color',
        'product_size',
        'stock',
        'created_at',
        'updated_at',
    ]

    list_filter = [
        'product_color__color',
        'product_size__size_type',
    ]

    ordering = ['-created_at']

    search_fields = [
        'product_color__product__title',
        'product_color__color__title',
        'product_size__title',
    ]

    readonly_fields = [
        'created_at',
        'updated_at',
    ]

    list_select_related = [
        'product_color',
        'product_color__product',
        'product_color__color',
        'product_size',
    ]

    empty_value_display = 'خالی'


@admin.register(ProductComment)
class CustomProductCommentAdmin(admin.ModelAdmin):
    """Configures the Django admin interface for product comments."""

    list_display = [
        'user',
        'product',
        'is_approved',
        'created_at',
        'published_at',
    ]

    fields = [
        'user',
        'product',
        'body',
        'is_approved',
        'published_at',
        'created_at',
        'updated_at',
    ]

    list_filter = [
        'is_approved',
        'created_at',
        'published_at',
    ]

    ordering = ['-created_at']

    search_fields = [
        'user__email',
        'product__title',
        'body',
    ]

    readonly_fields = [
        'created_at',
        'updated_at',
        'published_at',
    ]

    list_select_related = [
        'user',
        'product',
    ]

    actions = [
        'approve_comments',
    ]

    empty_value_display = 'خالی'

    @admin.action(description='تأیید نظرات انتخاب‌شده')
    def approve_comments(self, request, queryset):
        """Approves selected comments and sets their publication date."""

        unpublished_comments = queryset.filter(is_approved=False)

        unpublished_comments.update(
            is_approved=True,
            published_at=timezone.now(),
        )