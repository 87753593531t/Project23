from django.urls import path, re_path
from rest_framework.routers import DefaultRouter

from people.views import CarViewSet, CityViewSet, NameViewSet

router = DefaultRouter()

router.register('car', CarViewSet)
router.register('city', CityViewSet)
router.register('name', NameViewSet)

urlpatterns = [

]+ router.urls