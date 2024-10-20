from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from edblocks.models import Lesson, Module


class ModuleSerializer(ModelSerializer):
    class Meta:
        model = Module
        fields = "__all__"


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class ModuleDetailSerializer(ModelSerializer):
    lessons_in_module = SerializerMethodField()
    lesson = LessonSerializer(many=True, read_only=True, source="modules")

    def get_lessons_in_module(self, module):
        return Lesson.objects.filter(module=module).count()

    class Meta:
        model = Module
        fields = ("name", "description", "number", "author", "lessons_in_module", "lesson")

