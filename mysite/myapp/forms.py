from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from . import models

def must_be_caps(value):
    if not value.isupper():
        raise forms.ValidationError("Not all uppercase")
    # Always return the cleaned data, whether you have changed it or
    # not.
    return value

def must_be_unique(value):
    user = User.objects.filter(email=value)
    if len(user) > 0:
        raise forms.ValidationError("Email Already Exists")
    # Always return the cleaned data, whether you have changed it or
    # not.
    return value

def must_be_bob(value):
    if not value.startswith("BOB"):
        raise forms.ValidationError("Must start with 'BOB'")
    # Always return the cleaned data, whether you have changed it or
    # not.
    return value

class SuggestionForm(forms.Form):
    suggestion = forms.CharField(
        label='Suggestion',
        required=True,
        max_length=240,
    )

    image = forms.ImageField(
        label="Image File",
        required=False
    )
    image_description = forms.CharField(
        label='Image Description',
        max_length=240,
        required=False
    )

    def save(self, request):
        suggestion_instance = models.SuggestionModel()
        suggestion_instance.suggestion = self.cleaned_data["suggestion"]
        suggestion_instance.author = request.user
        suggestion_instance.image = self.cleaned_data["image"]
        suggestion_instance.image_description = self.cleaned_data["image_description"]
        suggestion_instance.save()
        return suggestion_instance

class CommentForm(forms.Form):
    comment = forms.CharField(
        label='Comment',
        required=True,
        max_length=240
    )

    def save(self, request, sugg_id):
        suggestion_instance = models.SuggestionModel.objects.filter(id=sugg_id).get()
        comment_instance = models.CommentModel()
        comment_instance.suggestion = suggestion_instance
        comment_instance.comment = self.cleaned_data["comment"]
        comment_instance.author = request.user
        comment_instance.save()
        return comment_instance

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        required=True,
        validators=[must_be_unique]
        )

    class Meta:
        model = User
        fields = ("username", "email",
                  "password1", "password2")

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
