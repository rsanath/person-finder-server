from django.urls import path, include
from rest_framework import routers
from .views import (
    ComplaintViewSet,
    SearcheeViewSet,
    SearcheeSampleViewSet,
    SearchViewSet,
    SearchResultViewSet
)

router = routers.DefaultRouter()

router.register('complaints', ComplaintViewSet)
router.register('searchees', SearcheeViewSet)
router.register('searchee_samples', SearcheeSampleViewSet)
router.register('searches', SearchViewSet)
router.register('search_results', SearchResultViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
