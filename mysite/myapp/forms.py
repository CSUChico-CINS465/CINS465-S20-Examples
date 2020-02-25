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
        raise forms.ValidationError("Must be bob")
    # Always return the cleaned data, whether you have changed it or
    # not.
    return value

class SuggestionForm(forms.Form):
    suggestion = forms.CharField(
        label='Suggestion',
        required=True,
        max_length=240
    )

    def save(self, request):
        suggestion_instance = models.SuggestionModel()
        suggestion_instance.suggestion = self.cleaned_data["suggestion"]
        suggestion_instance.author = request.user
        suggestion_instance.save()
        return suggestion_instance

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
