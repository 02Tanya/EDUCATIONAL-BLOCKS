from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from users.apps import UsersConfig
from django.urls import path
from rest_framework.routers import SimpleRouter
from users.models import User
from users.views import (
    UserListApiView,
    UserRetrieveApiView,
    UserCreateApiView,
    UserDestroyApiView,
    UserUpdateApiView,
)

app_name = UsersConfig.name


router = SimpleRouter()
# router.register("", UserViewSet)

urlpatterns = [
    path("user/", UserListApiView.as_view(), name="user_list"),
    path("user/<int:pk>/", UserRetrieveApiView.as_view(), name="user_retrieve"),
    path("user/create/", UserCreateApiView.as_view(), name="user_create"),
    path("user/<int:pk>/delete/", UserDestroyApiView.as_view(), name="user_delete"),
    path("user/<int:pk>/update/", UserUpdateApiView.as_view(), name="user_update"),
    path(
        "login/",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="login",
    ),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(permission_classes=(AllowAny,)),
        name="token_refresh",
    ),
]

urlpatterns += router.urls
