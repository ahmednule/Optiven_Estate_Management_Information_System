from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home_page'),
    path('properties/', views.property_list, name='property_list'),
    path('properties/<int:pk>/', views.property_detail, name='property_detail'),
    path('properties/<int:pk>/order/', views.order_property, name='order_property'),
    path('dashboard/', views.dashboard, name='dashboard'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)