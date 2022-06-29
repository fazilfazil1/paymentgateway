from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('checkout/',views.checkout),
    path('product/',views.product),
    path('add/',views.sampleform),
    path('result/',views.results)
]