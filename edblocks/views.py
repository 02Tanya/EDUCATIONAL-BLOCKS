from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

from edblocks.models import Lesson, Module
from edblocks.serializers import (
    LessonSerializer,
    ModuleSerializer,
    ModuleDetailSerializer,
)
from users.permissions import IsOwner


class ModuleViewSet(ModelViewSet):
    queryset = Module.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return ModuleDetailSerializer
        return ModuleSerializer

    def perform_create(self, serializer):
        course = serializer.save()
        course.author = self.request.user
        course.save()

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = (IsAuthenticated,)
        elif self.action == "retrieve":
            self.permission_classes = (AllowAny,)
        elif self.action == ["destroy", "update"]:
            self.permission_classes = (IsOwner,)
        return super().get_permissions()


class LessonCreateApiView(CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsOwner,)

    def perform_create(self, serializer):
        lesson = serializer.save()
        lesson.author = self.request.user
        lesson.save()


class LessonListApiView(ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (AllowAny,)
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('module', 'name')
    ordering_fields = ('module',)


class LessonRetrieveApiView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (AllowAny,)


class LessonUpdateApiView(UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsOwner,)


class LessonDestroyApiView(DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsOwner,)
