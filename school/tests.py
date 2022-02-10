from django.test import TestCase
from school.models import Student
from django.contrib.auth.models import User
from django.test import Client


class StudentTestCase(TestCase):
    def setUp(self):
        Student.objects.create(name='Zaurbek', surname='Tedeev', patronymic='Georgievich', age=19, user=User.objects.create(username='liling', password='123'))
        Student.objects.create(name='Ruslan', surname='Dzugaev', patronymic='Nikolaevich', age=19, user=User.objects.create(username='bober', password='123'))

    def test_full_name_student(self):
        zaur_tedeev = Student.objects.get(name='Zaurbek', surname='Tedeev')
        ruslan_dzugaev = Student.objects.get(name='Ruslan', surname='Dzugaev')

        self.assertEqual(zaur_tedeev.full_name, 'Tedeev Zaurbek Georgievich')
        self.assertEqual(ruslan_dzugaev.full_name, 'Dzugaev Ruslan Nikolaevich')

    def test_duplicate_login(self):
        with self.assertRaises(Exception):
            Student.objects.create(name='Zaurbek', surname='Tedeev', patronymic='Georgievich', age=19, user=User.objects.create(username='liling', password='123'))

class RoutingTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_all_endpoints(self):
        login_response = self.client.get('/')

        self.assertEqual(login_response.status_code, 200)

