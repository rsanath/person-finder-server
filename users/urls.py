from django.urls import path, include
from rest_framework import routers
from rest_framework_extensions.routers import NestedRouterMixin
from . import views
from searches.views import ComplaintViewSet


class NestedDefaultRouter(NestedRouterMixin, routers.DefaultRouter):
    pass

router = NestedDefaultRouter()

router.register('users', views.UserViewSet)
router.register('complaints', ComplaintViewSet, base_name='users-complaints')


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
