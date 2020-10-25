from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory

from .models import Event, Participant
from .views import index


class SimpleTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_details(self):
        # Create an instance of a GET request.
        request = self.factory.get("/")
        request.user = AnonymousUser()

        # Test my_view() as if it were deployed at /customer/details
        response = index(request)
        self.assertEqual(response.status_code, 200)


class EventParticipant(TestCase):
    def setUp(self):
        Event.objects.create(name="lion")
        Event.objects.create(name="cat")

    def participant(self):
        lion = Event.objects.get(name="lion")
        john = Participant.objects.create(name="John", event_key=lion)
        self.assertEqual(print(john), 'John')
