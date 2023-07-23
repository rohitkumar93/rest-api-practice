from django.contrib import admin
from rest_framework import routers
from django.urls import include, path
# from rest_framework import routers
# from currency import views as currviews
from piggybank import views
from rest_framework_simplejwt import views as jwt_views
from piggybank.serializers import CurrencySerializer
from rest_framework.authtoken.views import obtain_auth_token


router = routers.SimpleRouter()
router.register(r'categories', views.CategoryModelViewSet, basename="category")

# router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include(router.urls)),
    path('', include('quickstart.urls')),
    path("currencies/", views.CurrencyListAPIView.as_view(), name="currencies"),
    path('login', views.LoginView.as_view(), name='login'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
] + router.urls
