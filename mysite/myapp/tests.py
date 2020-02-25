from django.test import TestCase
from django.contrib.auth.models import User
from .models import Suggestion_Model

# Create your tests here.
class SuggestionTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        user.save()
        user = User.objects.get(id=1)
        Suggestion_Model.objects.create(suggestion="lion", author=user)
        Suggestion_Model.objects.create(suggestion="cat", author=user)

    def test_suggestion_to_string(self):
        lion = Suggestion_Model.objects.get(suggestion="lion")
        cat = Suggestion_Model.objects.get(suggestion="cat")
        self.assertEqual(str(lion), 'john lion')
        self.assertEqual(str(cat), 'john cat')

    def test_suggestion_author(self):
        lion = Suggestion_Model.objects.get(suggestion="lion")
        cat = Suggestion_Model.objects.get(suggestion="cat")
        self.assertEqual(lion.author.username, "john")
        self.assertEqual(cat.author.username, "john")

    def test_suggestion_suggestion(self):
        lion = Suggestion_Model.objects.get(suggestion="lion")
        cat = Suggestion_Model.objects.get(suggestion="cat")
        self.assertEqual(lion.suggestion, "lion")
        self.assertEqual(cat.suggestion, "cat")