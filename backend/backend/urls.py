from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet, GroupViewSet
from apps.core.api.viewsets import ListViewSet, ItemViewSet
from rest_framework.authtoken import views


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'list', ListViewSet, basename='list')
router.register(r'item', ItemViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/', views.obtain_auth_token, name='api-tokn-auth'),
]
