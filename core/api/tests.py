from django.test import TestCase, Client
from django.urls import reverse

class ActivitiesViewTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_get_activity(self):
        # Hacer una petición GET a la vista
        response = self.client.get(reverse('activity'))
        # Comprobar que el estado de la respuesta es 200
        self.assertEqual(response.status_code, 200)
        # Comprobar que la respuesta contiene un JSON válido
        json_data = response.json()
        self.assertIsInstance(json_data, dict)


class ActivityUpdateViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.activity = Activity.objects.create(
            activity="Learn how to use a french press",
            type="recreational",
            participants=1,
            price=0.3,
            link="https://en.wikipedia.org/wiki/French_press",
            key="4522866",
            accessibility=0.3
        )
    def test_patch_activity(self):
        data = {"done": True}
        response = self.client.patch(
            reverse('activity_update', kwargs={'id': self.activity.id}),
            json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 204)
        self.activity.refresh_from_db()
        self.assertTrue(self.activity.done)

class UserActivityViewSetTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='user1',
            email='user1@example.com',
            password='TestPass3'
        )
        self.activity = Activity.objects.create(
            user=self.user,
            activity="Learn how to use a french press",
            type="recreational",
            participants=1,
            price=0.3,
            link="https://en.wikipedia.org/wiki/French_press",
            key="4522866",
            accessibility=0.3
        )

    def test_list_user_activity(self):
        # Iniciar sesión como el usuario de prueba
        self.client.login(username='testuser', password='testpassword')
        # Hacer una petición GET a la vista
        response = self.client.get(reverse('user-activities'))
        # Comprobar que el estado de la respuesta es 200
        self.assertEqual(response.status_code, 200)
        # Comprobar que la respuesta contiene un JSON válido
        json_data = response.json()
        self.assertIsInstance(json_data, list)
        self.assertEqual(len(json_data), 1)
        self.assertEqual(json_data[0]['activity'], self.activity.activity)