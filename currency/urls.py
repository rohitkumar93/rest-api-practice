from django.urls import re_path as url
from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from django.urls import include, path
from piggybank import views
from rest_framework_simplejwt import views as jwt_views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.urlpatterns import format_suffix_patterns
from todo import views as todoviews
from new_todo import views as newtodo_views

router = routers.DefaultRouter()

router.register(r'tasks', newtodo_views.TodoView, 'task')


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('quickstart.urls')),
    path("currencies/", views.CurrencyListAPIView.as_view(), name="currencies"),
    path('login', views.LoginView.as_view(), name='login'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('todo_api/', include(router.urls)),
    path('todo_api/<int:id>/',
         newtodo_views.TodoDefineView.as_view())
]

todourlpatterns = [
    url(r'^todo_lists$', todoviews.TodoList.as_view()),
    url(r'^todo_lists/(?P<todo_list_id>[0-9]+)$',
        todoviews.TodoList.as_view()),
    url(r'^todo_lists/(?P<todo_list_id>[0-9]+)/items$',
        todoviews.TodoListItem.as_view()),
    url(r'^todo_lists/items/(?P<todo_list_item_id>[0-9]+)$',
        todoviews.TodoListItem.as_view()),
]


todourlpatterns = format_suffix_patterns(todourlpatterns)
