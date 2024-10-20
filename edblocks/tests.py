from django.urls import reverse
from rest_framework import status

from rest_framework.test import APITestCase, APIClient

from edblocks.models import Lesson, Module
from users.models import User


class LessonAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='test22@test.ru')
        self.client.force_authenticate(user=self.user)

        self.course = Module.objects.create(
            number=1,
            name='Лесные заклятья',
            description='Самое лучшее колдовство в лесу',
            author=self.user
        )
        self.lesson = Lesson.objects.create(
            name='Лесные приметы',
            description='Самые действенные лесные приметы',
            module=self.course,
        )


    def test_lesson_retrieve(self):
        '''Тестирование просмотра данных об уроке.'''
        url = reverse("edblocks:lessons_retrieve", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.lesson.name)


    def test_lesson_create(self):
        '''Тестирование создания урока.'''
        url = reverse("edblocks:lessons_create")
        data = {
            "name": "Колдовские зелья",
            "description": "Основы изготовления зелий",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)


    def test_lesson_update(self):
        '''Тестирование обновления данных урока.'''
        url = reverse("edblocks:lessons_update", args=(self.lesson.pk,))
        data = {
            "name": "Колдовские зелья и варево"
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), "Колдовские зелья и варево")


    def test_lesson_delete(self):
        '''Тестирование удаления урока.'''
        url = reverse("edblocks:lessons_delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)


    def test_lesson_list(self):
        '''Тестирование просмотра списка уроков.'''
        url = reverse("edblocks:lessons_list")
        response = self.client.get(url)
        data = response.json()
        result = {
                'count': 1,
                'next': None,
                'previous': None,
                'results': [
                    {
                        'id': self.lesson.pk,
                        'name': self.lesson.name,
                        'description': self.lesson.description,
                        'module': self.course.pk,
                    }
                ]
            }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

