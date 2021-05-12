from django.urls import path
from . import views
from django.conf import settings
from django.urls import re_path
from django.views.static import serve


urlpatterns = [

    path('', views.products, name='products'),
    path('add_to_cart/', views.add_to_cart, name='add-to-cart'),
    path('product_detail/<int:id>', views.product_detail, name='product_detail'),
    path('search/', views.search, name='search'),

]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
