from django.contrib import admin
from django.urls import path
from django.urls import include, path
from rest_framework import routers
from currency import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include(router.urls)),
    path('', include('quickstart.urls')),
]
