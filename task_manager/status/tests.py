from django.test import TestCase
from task_manager.status.models import Status
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse


class TestStatus(TestCase):

    def setUp(self):
        self.client.force_login(User.objects.get_or_create(username='testuser')[0])  # noqa: E501

    def test_status_index(self):
        response = self.client.get('/statuses/')
        self.assertEqual(response.status_code, 200)

    def test_status_create(self):
        response = self.client.get(reverse('statuses_create'))
        self.assertEqual(response.status_code, 200)

    def test_status_update(self):
        status_obj = Status()
        status_obj.name = 'IgOgO'
        status_obj.save()
        response = self.client.get('/statuses/1/update/')
        self.assertEqual(response.status_code, 200)

    def test_status_delete(self):
        status_obj = Status()
        status_obj.name = 'IgOgO'
        status_obj.save()
        response = self.client.post('/statuses/1/delete/')
        try:
            Status.objects.get(id=1)
            object_deleted = False
        except ObjectDoesNotExist:
            object_deleted = True
        self.assertTrue(object_deleted)
        self.assertEqual(response.status_code, 302)
