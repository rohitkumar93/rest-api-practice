from django.contrib import admin
from rest_framework import routers
from django.urls import include, path
# from rest_framework import routers
# from currency import views as currviews
from piggybank import views
from piggybank.serializers import CurrencySerializer


router = routers.SimpleRouter()
router.register(r'categories', views.CategoryModelViewSet, basename="category")

# router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include(router.urls)),
    path('', include('quickstart.urls')),
    path("currencies/", views.CurrencyListAPIView.as_view(), name="currencies"),
] + router.urls
