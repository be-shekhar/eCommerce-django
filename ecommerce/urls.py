from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from products.views import (
    ProductListView, ProductDetailView, ProductFeaturedListView,
    ProductFeaturedDetailView, ProductDetailSlugView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', ProductListView.as_view(), name='product-list-view'),
    path('featured/', ProductFeaturedListView.as_view(), name='product-featured-list-view'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail-view'),
    path('products/<slug:title>/', ProductDetailSlugView.as_view(), name='product-detail-slug-view'),
    path(
        'featured/<int:pk>/', 
        ProductFeaturedDetailView.as_view(), 
        name='product-featured-detail-view'
    ),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
    urlpatterns = urlpatterns + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )