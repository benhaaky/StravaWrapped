from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'authcode', views.AuthCodeViewSet, basename='authcode')
router.register(r'athlete', views.AthleteViewSet)
router.register(r'activity', views.ActivityViewSet, basename='activity')
router.register(r'map', views.MapViewSet)
router.register(r'token', views.TokenViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
