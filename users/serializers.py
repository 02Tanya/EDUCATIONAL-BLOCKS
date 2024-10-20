from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from users.models import User

from django.contrib.auth import get_user_model

# User = get_user_model()


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


# class UserSerializer(ModelSerializer):
#     class Meta:
#         model = User
#         fields = ("email", "password")


