from django.contrib import admin
from edblocks.models import Module, Lesson


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "number", "author")


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "module")

