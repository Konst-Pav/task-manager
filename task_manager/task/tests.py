from django.test import TestCase
from django.urls import reverse_lazy, reverse
from task_manager.task.models import Task
from task_manager.status.models import Status
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


class TestTask(TestCase):

    def setUp(self):
        self.client.force_login(User.objects.get_or_create(username='testuser')[0])
        user1 = User.objects.create_user(
            username='user1',
            first_name='Ivan',
            last_name='Petrov',
            # password1='Parol123',
            # password2='Parol123',
        )
        user2 = User.objects.create_user(
            username='user2',
            first_name='Tatyana',
            last_name='Sidorova',
            # password1='Parol123',
            # password2='Parol123',
        )
        status1 = Status.objects.create(name='status1')
        status2 = Status.objects.create(name='status1')
        task1 = Task.objects.create(
            name='task1_name',
            description='description',
            executor=user1,
            status=status1,
            author=user2,
        )
        task2 = Task.objects.create(
            name='task2_name',
            description='description',
            executor=user2,
            status=status2,
            author=user1,
        )

    def test_task_index_page_is_available(self):
        response = self.client.get(reverse('tasks_index'))
        self.assertEqual(response.status_code, 200)

    def test_task_index_data_is_correct(self):
        response = self.client.get(reverse('tasks_index'))
        content = response.content.decode()
        task_data = ['task1_name', 'task2_name']
        data_is_correct = False
        for item in task_data:
            if item in content:
                data_is_correct = True
            else:
                data_is_correct = False
                break
        self.assertTrue(data_is_correct)

    def test_task_index_login_required(self):
        self.client.logout()
        response = self.client.get(reverse('tasks_index'))
        redirect_path = f'{reverse("login_view")}?next={reverse("tasks_index")}'
        self.assertRedirects(response, expected_url=redirect_path)

    def test_task_create_page_is_available(self):
        response = self.client.get(reverse('tasks_create'))
        self.assertEqual(response.status_code, 200)

    def test_task_create_login_required(self):
        self.client.logout()
        response = self.client.get(reverse('tasks_create'))
        redirect_path = f'{reverse("login_view")}?next={reverse("tasks_create")}'
        self.assertRedirects(response, expected_url=redirect_path)

    def test_task_create_task_created(self):
        test_task_data = {
            'name': 'test_task_name',
            'description': 'test_task_description',
            'executor': 2,
            'status': 1,
        }
        self.client.post(reverse('tasks_create'), data=test_task_data)
        try:
            Task.objects.get(name=test_task_data['name'])
            task_created = True
        except ObjectDoesNotExist:
            task_created = False
        self.assertTrue(task_created)

    def test_task_read_page_is_available(self):
        response = self.client.get(reverse('tasks_read', args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_task_read_data_is_correct(self):
        task_obj = Task.objects.get(id=1)
        task_data = [task_obj.name, task_obj.description, task_obj.executor, task_obj.status, task_obj.author]
        response = self.client.get(reverse('tasks_read', args=[1]))
        content = response.content.decode()
        data_is_correct = False
        for item in task_data:
            if str(item) in content:
                data_is_correct = True
            else:
                data_is_correct = False
                break
        self.assertTrue(data_is_correct)

    def test_task_read_login_required(self):
        self.client.logout()
        response = self.client.get(reverse('tasks_read', args=[1]))
        redirect_path = f'{reverse("login_view")}?next={reverse("tasks_read", args=[1])}'
        self.assertRedirects(response, expected_url=redirect_path)

    def test_task_update_page_is_available(self):
        response = self.client.get(reverse('tasks_update', args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_task_update_login_required(self):
        self.client.logout()
        response = self.client.get(reverse('tasks_update', args=[1]))
        redirect_path = f'{reverse("login_view")}?next={reverse("tasks_update", args=[1])}'
        self.assertRedirects(response, expected_url=redirect_path)

    def test_task_update_task_updated(self):
        executor = User.objects.get(id=1)
        status = Status.objects.get(id=1)
        task_obj = Task.objects.create(
            name='Test task',
            description='Test description',
            executor=executor,
            status=status,
        )
        new_data = {
            'name': 'Updated name',
            'description': 'Updated description',
            'executor': 2,
            'status': 2,
        }
        self.client.post(reverse_lazy('tasks_update', args=[task_obj.id]), data=new_data)
        updated_task_obj = Task.objects.get(id=task_obj.id)
        self.assertEqual(new_data['name'], updated_task_obj.name)
        self.assertEqual(new_data['description'], updated_task_obj.description)
        self.assertEqual(new_data['executor'], updated_task_obj.executor.id)
        self.assertEqual(new_data['status'], updated_task_obj.status.id)

    def test_task_delete_page_is_available(self):
        response = self.client.get(reverse('tasks_delete', args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_task_delete_login_required(self):
        self.client.logout()
        response = self.client.get(reverse('tasks_delete', args=[1]))
        redirect_path = f'{reverse("login_view")}?next={reverse("tasks_delete", args=[1])}'
        self.assertRedirects(response, expected_url=redirect_path)

    def test_task_delete_task_deleted(self):
        author = User.objects.get(id=1)
        status = Status.objects.get(id=1)
        task_obj = Task.objects.create(name='Test task', author=author, status=status)
        self.client.post(reverse_lazy('tasks_delete', args=[task_obj.id]))
        try:
            Task.objects.get(id=task_obj.id)
            task_deleted = False
        except ObjectDoesNotExist:
            task_deleted = True
        self.assertTrue(task_deleted)
