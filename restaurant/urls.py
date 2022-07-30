from django.urls import path
from .views import *

urlpatterns = [
    path('create/', CreateRestaurantAPIView.as_view(), name='create-restaurant'),
    path('restaurants/', ListRestaurantAPIView.as_view(), name='list-restaurant'),
    path('create-menu/', CreateMenuAPIView.as_view(), name='create-menu'),
    path('menu/<str:day>/', GetMenuAPIView.as_view(), name='list-menu'),
    path('menus/', ListMenuAPIView.as_view(), name='list-menus')
]
