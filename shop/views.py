from django.views.generic import (TemplateView,
                                  ListView,
                                  DetailView)

from shop.models import ProductModel, ProductSizeModel, ProductComment
from shop.choices import ProductStatusType

# Create your views here.


class ProductDetailView(DetailView):
    """Display the details of a published product."""

    template_name = 'shop/product-detail.html'

    queryset = ProductModel.objects.filter(
        status=ProductStatusType.PUBLISHED
    )

    slug_url_kwarg = 'slug'
    context_object_name = 'product'

    def get_queryset(self):
        """Optimize queries for product colors, images, and variants."""
        return super().get_queryset().prefetch_related(
            'product_colors__color',
            'product_colors__images',
            'product_colors__variants__product_size',
        )


    def get_context_data(self, **kwargs):
        """Add product color images and approved comments to the template context."""
        context = super().get_context_data(**kwargs)

        color_images = []

        for product_color in self.object.product_colors.all():
            images = [
                {
                    'url': image.image.url,
                    'alt': image.alt_text,
                }
                for image in product_color.images.all()
            ]

            color_images.append({
                'id': product_color.id,
                'images': images,
            })

        context['color_images'] = color_images

        context['comments'] = ProductComment.objects.filter(
            product=self.object,
            is_approved=True
        )


        context['similar_products'] = ProductModel.objects.filter(
            status=ProductStatusType.PUBLISHED,
            category=self.object.category
        ).exclude(
            id=self.object.id
        )[:8]

        return context
