from django.shortcuts import render

from catalog.models import Product


# Create your views here.
def contacts(request):
    return render(request, 'catalog/contacts.html')


def home(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list
    }
    return render(request, 'catalog/home.html', context)

def goods(request):
    return render(request, 'catalog/goods.html')