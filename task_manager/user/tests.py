from django.test import TestCase
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


class TestUserViews(TestCase):

    def test_user_index(self):
        response = self.client.get(reverse('users_index'))
        self.assertEqual(response.status_code, 200)

    def test_user_create(self):
        response = self.client.get(reverse('users_create'))
        self.assertEqual(response.status_code, 200)
        test_user = {
            'username': 'test_username',
            'first_name': 'test_user',
            'last_name': 'test_user',
            'password1': 'Parol123',
            'password2': 'Parol123'}
        response = self.client.post(reverse('users_create'), data=test_user)
        self.assertEqual(response.status_code, 302)

    def test_user_update(self):
        test_user = User.objects.create_user(username='test_username')
        response = self.client.get(reverse('users_update', args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_user_delete(self):
        test_user = User.objects.create_user(username='test_username')
        response = self.client.get(reverse('users_delete', args=[test_user.id]))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(reverse('users_delete', args=[test_user.id]))
        try:
            deleted_user = User.objects.get(id=test_user.id)
            object_deleted = False
        except ObjectDoesNotExist:
            object_deleted = True
        self.assertTrue(object_deleted)
        self.assertEqual(response.status_code, 302)

    def test_user_login(self):
        pass
