from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from catalog.views import home, contacts

app_name = 'catalog'

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
