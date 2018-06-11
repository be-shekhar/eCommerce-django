# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import Http404
from django.shortcuts import get_object_or_404

from products.models import Product


class ProductListView(ListView):
    ''' A generic product listing view '''
    # default -> template_name = "products/product_list.html"
    # default -> object_list for context
    queryset = Product.objects.all()
    template_name = "products/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        print("ProductListView Context:", context)
        return context


class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_object(self, *args, **kwargs):
        slug = self.kwargs.get('title')
        instance = get_object_or_404(Product, slug=slug)
        return instance


class ProductDetailView(DetailView):
    ''' A generic product detailing view '''
    # queryset = Product.objects.all() Not required since we have overridden get_object method
    # We can override get_queryset method as well. Guess what it does!!
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print("ProductDetailView Context:", context)
        # We can manipulate context here and send it to the calling function.
        return context
    
    def get_object(self, *args, **kwargs):
        # request instance is stored in self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(id=pk)
        if instance is None:
            raise Http404("Product doesn't exists! :(")
        return instance


class ProductFeaturedListView(ListView):
    template_name = "products/list.html"

    def get_queryset(self, *args, **kwargs):
        return Product.objects.all().featured()


class ProductFeaturedDetailView(DetailView):
    template_name = "products/featured-detail.html"

    def get_queryset(self, *args, **kwargs):
        return Product.objects.featured()