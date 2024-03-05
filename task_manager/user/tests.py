from django.test import TestCase
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


class TestUserViews(TestCase):

    def setUp(self):
        authorized_user = User.objects.create_user(username='authorized_user')
        self.client.force_login(authorized_user)
        User.objects.create_user(username='Kolya')
        User.objects.create_user(username='Tonya')
        User.objects.create_user(username='Sonya')

    def test_user_index_page_is_available(self):
        response = self.client.get(reverse('users_index'))
        self.assertEqual(response.status_code, 200)

    def test_user_index_data_is_correct(self):
        response = self.client.get(reverse('users_index'))
        data = list(User.objects.values('username'))
        content = response.content.decode()
        data_is_correct = False
        for user in data:
            if user['username'] in content:
                data_is_correct = True
            else:
                data_is_correct = False
                break
        self.assertTrue(data_is_correct)

    def test_user_create_page_is_available(self):
        response = self.client.get(reverse('labels_create'))
        self.assertEqual(response.status_code, 200)

    def test_user_create_user_created(self):
        user_data = {
            'username': 'Vanya',
            'first_name': 'Vanyusha',
            'last_name': 'Ivanov',
            'password1': 'Parol123',
            'password2': 'Parol123',
        }
        self.client.post(reverse_lazy('users_create'), data=user_data)
        try:
            User.objects.get(username=user_data['username'])
            user_created = True
        except ObjectDoesNotExist:
            print('ObjectDoesNotExist')
            user_created = False
        self.assertTrue(user_created)

    def test_user_update_page_is_available(self):
        response = self.client.get(reverse('users_update', args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_user_update_login_required(self):
        self.client.logout()
        response = self.client.get(reverse('users_update', args=[1]))
        redirect_path = f'{reverse("login_view")}?next={reverse("users_update", args=[1])}'
        self.assertRedirects(response, expected_url=redirect_path)

    def test_user_delete_page_is_available(self):
        response = self.client.get(reverse('users_delete', args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_user_delete_user_deleted(self):
        self.client.post(reverse_lazy('users_delete', args=[1]))
        try:
            User.objects.get(id=1)
            label_deleted = False
        except ObjectDoesNotExist:
            label_deleted = True
        self.assertTrue(label_deleted)

    def test_user_delete_login_required(self):
        self.client.logout()
        response = self.client.get(reverse('users_delete', args=[1]))
        redirect_path = f'{reverse("login_view")}?next={reverse("users_delete", args=[1])}'
        self.assertRedirects(response, expected_url=redirect_path)
