from django.db import models
from django.conf import settings


class Module(models.Model):
    number = models.PositiveIntegerField(
        unique=True,
        verbose_name="Номер модуля",
        help_text="Введите номер модуля",
    )
    name = models.CharField(
        max_length=100,
        verbose_name="Название модуля",
        help_text="Введите название модуля",
    )
    description = models.TextField(
        verbose_name="Описание модуля",
        help_text="Введите описание модуля",
        null=True,
        blank=True,
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Автор",
        help_text="Укажите автора",
    )

    class Meta:
        verbose_name = "Образовательный модуль"
        verbose_name_plural = "Образовательные модули"
        ordering = ["number"]

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название урока",
        help_text="Введите название урока",
    )
    description = models.TextField(
        verbose_name="Описание урока",
        help_text="Введите описание урока",
        null=True,
        blank=True,
    )
    module = models.ForeignKey(
        Module,
        on_delete=models.CASCADE,
        verbose_name="Модуль",
        help_text="Введите название модуля",
        null=True,
        blank=True,
        related_name="modules",
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Автор",
        help_text="Укажите автора",
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
        ordering = ["name", "module"]

    def __str__(self):
        return self.name
