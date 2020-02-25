from django.test import TestCase
from django.contrib.auth.models import User
from .models import SuggestionModel

# Create your tests here.
class SuggestionTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        user.save()
        user = User.objects.get(id=1)
        SuggestionModel.objects.create(suggestion="lion", author=user)
        SuggestionModel.objects.create(suggestion="cat", author=user)

    def test_suggestion_to_string(self):
        lion = SuggestionModel.objects.get(suggestion="lion")
        cat = SuggestionModel.objects.get(suggestion="cat")
        self.assertEqual(str(lion), 'john lion')
        self.assertEqual(str(cat), 'john cat')

    def test_suggestion_author(self):
        lion = SuggestionModel.objects.get(suggestion="lion")
        cat = SuggestionModel.objects.get(suggestion="cat")
        self.assertEqual(lion.author.username, "john")
        self.assertEqual(cat.author.username, "john")

    def test_suggestion_suggestion(self):
        lion = SuggestionModel.objects.get(suggestion="lion")
        cat = SuggestionModel.objects.get(suggestion="cat")
        self.assertEqual(lion.suggestion, "lion")
        self.assertEqual(cat.suggestion, "cat")
