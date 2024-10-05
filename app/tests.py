import json

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from app.models import Pereval, MyUser, Coords, Level, Images
from app.serializers import PerevalSerializer

'''python manage.py test . - Запускает все тесты
 python manage.py test app.tests.PerevalApiTestCase.test_get_list - для запуска одного конкретного теста
 coverage run --source='.' manage.py test . - создает слепок .coverage, при изменении теста команду повторить
 coverage report - по слепку создает отчет в консоли
coverage html - создает папку htmlcov\index.html и в ней отчет
 '''


class PerevalApiTestCase(APITestCase):
    def setUp(self):
        self.user_1 = MyUser.objects.create(email="test@test.ru", fam="Иванов", name="Иван", otc="Иванович",
                                           phone="88000000000")
        self.coords_1 = Coords.objects.create(latitude="45.3842", longitude="7.1525", height="1200")
        self.level_1 = Level.objects.create(winter="1A", summer="1A", autumn="1A", spring="1A", )
        self.pereval_1 = Pereval.objects.create(beauty_title="perev.", title="123gora", connect="connect",
                                                user=self.user_1, coords=self.coords_1, level=self.level_1)
        self.images_1 = Images.objects.create(pereval=self.pereval_1, )

    def test_get_list(self):
        url = reverse("pereval-list")
        response = self.client.get(url)
        serializer_data = PerevalSerializer([self.pereval_1, ], many=True).data
        self.assertEquals(serializer_data, response.data)
        self.assertEquals(status.HTTP_200_OK, response.status_code)

    def test_get_detail(self):
        url = reverse("pereval-detail", args=(self.pereval_1.id,))
        response = self.client.get(url)
        serializer_data = PerevalSerializer(self.pereval_1).data
        self.assertEquals(serializer_data, response.data)
        self.assertEquals(status.HTTP_200_OK, response.status_code)

    def test_user_update(self):
        url = reverse("pereval-detail", args=(self.pereval_1.id,))
        data = {
            "id": 3,
            "beauty_title": "perev.2",
            "title": "123gora2",
            "other_titles": "pereval2",
            "connect": "connect2",
            "user": {
                "email": "test@test.ru",
                "fam": "Изменено",
                "name": "Изменено",
                "otc": "Изменено",
                "phone": "Изменено"
            },
            "coords": {
                "latitude": "45.38420000",
                "longitude": "7.15250000",
                "height": "1200"
            },
            "images": [
                {
                    "data": "https://www.yandex.ru/search.jpg",
                    "title": "Спуск"
                },
                {
                    "data": "https://www.yandex.ru/search.jpg",
                    "title": "Подъём"
                }
            ],
        }
        json_data = json.dumps(data)
        response = self.client.patch(path=url, content_type='application/json', data=json_data)
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.pereval_1.refresh_from_db()
        self.assertEquals("test@test.ru", self.pereval_1.user.email)
        self.assertEquals("Иванов", self.pereval_1.user.fam)
        self.assertEquals("Иван", self.pereval_1.user.name)
        self.assertEquals("Иванович", self.pereval_1.user.otc)

    def test_pereval_update(self):
        url = reverse("pereval-detail", args=(self.pereval_1.id,))
        data = {
            "id": 3,
            "beauty_title": "Изменено",
            "title": "Изменено",
            "other_titles": "Изменено",
            "connect": "Изменено",
            "user": {
                "email": "test@test.ru",
                "fam": "Изменено",
                "name": "Изменено",
                "otc": "Изменено",
                "phone": "88000000000"
            },
            "coords": {
                "latitude": "45.38420000",
                "longitude": "7.15250000",
                "height": "1200"
            },
            "images": [
                {
                    "data": "https://www.yandex.ru/search.jpg",
                    "title": "Спуск"
                },
                {
                    "data": "https://www.yandex.ru/search.jpg",
                    "title": "Подъём"
                }
            ],
        }
        json_data = json.dumps(data)
        response = self.client.patch(path=url, content_type='application/json', data=json_data)
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.pereval_1.refresh_from_db()
        self.assertEquals("perev.", self.pereval_1.beauty_title)


class PerevalSerializerTestCase(TestCase):
    def setUp(self):
        self.user_1 = MyUser.objects.create(email="test@test.ru", fam="Иванов", name="Иван", otc="Иванович",
                                           phone="88000000000")
        self.coords_1 = Coords.objects.create(latitude="45.3842", longitude="7.1525", height="1200")
        self.level_1 = Level.objects.create(winter="1A", summer="1A", autumn="1A", spring="1A", )
        self.pereval_1 = Pereval.objects.create(beauty_title="perev.", title="123gora", other_titles="pereval",
                                                connect="connect", add_time='21-08-2024 04:05:02', user=self.user_1, coords=self.coords_1,
                                                level=self.level_1, )
        self.images_1 = Images.objects.create(pereval=self.pereval_1, data="https://www.yandex.ru/search.jpg",
                                              title="Спуск")

    def test_check(self):
        serializer_data = PerevalSerializer(self.pereval_1).data
        time = self.pereval_1.add_time.strftime('%d-%m-%Y %H:%M:%S')
        expected_data = {
            "id": 5,
            "beauty_title": "perev.",
            "title": "123gora",
            "other_titles": "pereval",
            "connect": "connect",
            "add_time": f"{time}",
            "user": {
                "email": "test@test.ru",
                "fam": "Иванов",
                "name": "Иван",
                "otc": "Иванович",
                "phone": "88000000000"
            },
            "coords": {
                "latitude": "45.3842",
                "longitude": "7.1525",
                "height": "1200"
            },
            "level": {
                "winter": "1A",
                "summer": "1A",
                "autumn": "1A",
                "spring": "1A"
            },
            "images": [
                {
                    "data": "https://www.yandex.ru/search.jpg",
                    "title": "Спуск"
                }
            ],
            "status": "new"
        }
        self.assertEquals(serializer_data, expected_data)
