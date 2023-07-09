from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from blog.views import BlogListView, BlogCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView
from catalog.views import contacts, ProductListView, ProductDetailView

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('view/<int:pk>', ProductDetailView.as_view(), name='goods'),
    path('blog/', BlogListView.as_view(), name='list'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('view/<int:pk>', BlogDetailView.as_view, name='view'),
    path('edit/<int:pk>', BlogUpdateView.as_view, name='edit'),
    path('delete/<int:pk>', BlogDeleteView.as_view, name='delete'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
