from django.shortcuts import render
from django.views.generic import ListView, DetailView

from catalog.models import Product


# Create your views here.
def contacts(request):
    return render(request, 'catalog/contacts.html')

class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/goods.html'
