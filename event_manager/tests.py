from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory

from .views import index


# Create your tests here.
def test_all():
    event_tests = event_test()
    event_tests.all()

    participant_tests = participant_test()
    participant_tests.all()
    pass


class event_test(TestCase):
    def set_up(self):
        self.factory = RequestFactory()

    def all(self):
        self.event_creation()
        self.add_events()
        self.filter_events()

    def event_creation(self):
        return

    # TODO
    # existing event -> return: False
    # no Input -> exception: no input found
    def add_events(self):
        return

    # TODO
    # existing input -> return: True
    # no Input -> exception: no input found
    # non-existing -> exception: item(s) not found
    def filter_events(self):
        return


class participant_test(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def all(self):
        self.participant_creation()
        self.add_participant()
        self.get_participants()

    def participant_creation(self):
        return

    # TODO
    # No participants -> exception: item(s) not found
    def get_participants(self):
        return

    # TODO
    # existing input -> return: True
    # no Input -> exception: no input found
    # non-existing event -> exception: item not found
    def add_participant(self):
        return


class view_test(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def all(self):
        pass

# class SimpleTest(TestCase):
#     def setUp(self):
#         # Every test needs access to the request factory.
#         self.factory = RequestFactory()
#
#     def test_details(self):
#         # Create an instance of a GET request.
#         request = self.factory.get("/")
#         request.user = AnonymousUser()
#
#         # Test my_view() as if it were deployed at /customer/details
#         response = index(request)
#         self.assertEqual(response.status_code, 200)
