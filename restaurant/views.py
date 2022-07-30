from .serializers import RestaurantSerializer, MenuSerializer
from .models import Restaurant, Menu
from rest_framework.permissions import *
from rest_framework import generics, views
from rest_framework import filters
from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from django.core.cache.backends.base import DEFAULT_TIMEOUT

# set cache settings
CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


# Create Restaurant API View
class CreateRestaurantAPIView(generics.CreateAPIView):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()
    permission_class = [AllowAny]


# List Restaurants API View
class ListRestaurantAPIView(generics.ListAPIView):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()
    permission_class = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    """
    cache functions
    """

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60 * 60))
    def dispatch(self, *args, **kwargs):
        return super(ListRestaurantAPIView, self).dispatch(*args, **kwargs)


# Create Manu API View
class CreateMenuAPIView(generics.CreateAPIView):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()
    permission_class = [AllowAny]


# List Menu API View
class ListMenuAPIView(generics.ListAPIView):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()
    permission_class = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['day', 'restaurant']

    """
    cache functions
    """

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60 * 60))
    def dispatch(self, *args, **kwargs):
        return super(ListMenuAPIView, self).dispatch(*args, **kwargs)


# List Menu API View
class GetMenuAPIView(generics.RetrieveAPIView):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()
    permission_class = [AllowAny]
    lookup_field = 'day'

    """
    cache functions
    """

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60 * 60))
    def dispatch(self, *args, **kwargs):
        return super(GetMenuAPIView, self).dispatch(*args, **kwargs)
