from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from catalog.views import contacts, ProductListView, ProductDetailView

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('view/<int:pk>', ProductDetailView.as_view(), name='goods'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
