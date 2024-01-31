from django.test import TestCase
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from task_manager.label.models import Label
from task_manager.task.models import Task
from task_manager.status.models import Status
from django.core.exceptions import ObjectDoesNotExist


class TestLabel(TestCase):
    def setUp(self):
        self.client.force_login(User.objects.get_or_create(username='testuser')[0])
        Label.objects.create(name='bug')
        Label.objects.create(name='invalid')
        Label.objects.create(name='question')

    def test_label_index_page_is_available(self):
        response = self.client.get(reverse('labels_index'))
        self.assertEqual(response.status_code, 200)

    def test_label_index_data_is_correct(self):
        response = self.client.get(reverse('labels_index'))
        data = list(Label.objects.values('name'))
        content = response.content.decode()
        data_is_correct = False
        for item in data:
            if item['name'] in content:
                data_is_correct = True
            else:
                data_is_correct = False
                break
        self.assertTrue(data_is_correct)

    def test_label_index_login_required(self):
        self.client.logout()
        response = self.client.get(reverse('labels_index'))
        redirect_path = f'{reverse("login_view")}?next={reverse("labels_index")}'
        self.assertRedirects(response, expected_url=redirect_path)

    def test_label_create_page_is_available(self):
        response = self.client.get(reverse('labels_create'))
        self.assertEqual(response.status_code, 200)

    def test_label_create_label_created(self):
        label_data = {'name': 'new label'}
        self.client.post(reverse_lazy('labels_create'), data=label_data)
        try:
            Label.objects.get(name=label_data['name'])
            label_created = True
        except ObjectDoesNotExist:
            label_created = False
        self.assertTrue(label_created)

    def test_label_create_login_required(self):
        self.client.logout()
        response = self.client.get(reverse('labels_create'))
        redirect_path = f'{reverse("login_view")}?next={reverse("labels_create")}'
        self.assertRedirects(response, expected_url=redirect_path)

    def test_label_update_page_is_available(self):
        response = self.client.get(reverse('labels_update', args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_label_update_label_updated(self):
        label = Label.objects.create(name='label_name')
        new_data = {'name': 'new_label_name'}
        self.client.post(reverse_lazy('labels_update', args=[label.id]), data=new_data)
        updated_label = Label.objects.get(id=label.id)
        self.assertEqual(new_data['name'], updated_label.name)

    def test_label_update_login_required(self):
        self.client.logout()
        response = self.client.get(reverse('labels_update', args=[1]))
        redirect_path = f'{reverse("login_view")}?next={reverse("labels_update", args=[1])}'
        self.assertRedirects(response, expected_url=redirect_path)

    def test_label_delete_page_is_available(self):
        response = self.client.get(reverse('labels_delete', args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_label_delete_label_deleted(self):
        label = Label.objects.create(name='new_label')
        self.client.post(reverse_lazy('labels_delete', args=[label.id]))
        try:
            Label.objects.get(id=label.id)
            label_deleted = False
        except ObjectDoesNotExist:
            label_deleted = True
        self.assertTrue(label_deleted)

    def test_label_delete_login_required(self):
        self.client.logout()
        response = self.client.get(reverse('labels_delete', args=[1]))
        redirect_path = f'{reverse("login_view")}?next={reverse("labels_delete", args=[1])}'
        self.assertRedirects(response, expected_url=redirect_path)
