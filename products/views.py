# from django.shortcuts import render
from django.views.generic import ListView

from products.models import Product


class ProductListView(ListView):
    ''' A generic product listing view '''
    # default -> template_name = "products/product_list.html"
    # default -> object_list for context
    queryset = Product.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        print("ProductListView Context:", context)
        return context

