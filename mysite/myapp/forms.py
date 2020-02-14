from django import forms
from django.core.validators import validate_slug


from . import models

def must_be_caps(value):
    if not value.isupper():
        raise forms.ValidationError("Not all uppercase")
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

    def save(self,request):
        suggestion_instance = models.Suggestion_Model()
        suggestion_instance.suggestion = self.cleaned_data["suggestion"]
        suggestion_instance.author=request.user
        suggestion_instance.save()
        return suggestion_instance