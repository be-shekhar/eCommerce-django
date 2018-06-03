# from django.shortcuts import render
from django.views.generic import ListView, DetailView

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


class ProductDetailView(DetailView):
    ''' A generic product detailing view '''
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print("ProductDetailView Context:", context)
        # We can manipulate context here and send it to the calling function.
        return context