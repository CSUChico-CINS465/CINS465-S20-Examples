from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from . import models
from . import forms

def logout_view(request):
    logout(request)
    return redirect("/")

# Create your views here.
def index(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            form = forms.SuggestionForm(request.POST)
            if form.is_valid():
                form.save(request)
                form = forms.SuggestionForm()
        else:
            form = forms.SuggestionForm()
    else:
        form = forms.SuggestionForm()
    suggestion_objects = models.Suggestion_Model.objects.all()
    suggestion_list=[]
    for sugg in suggestion_objects:
        comment_objects = models.CommentModel.objects.filter(suggestion=sugg)
        temp_sugg = {}
        temp_sugg["suggestion"]=sugg.suggestion
        temp_sugg["author"]=sugg.author.username
        temp_sugg["comments"]=comment_objects
        suggestion_list+=[temp_sugg]

    context = {
        "title":"Tempate Demo",
        "body":"<p> Hello Body</p>",
        "suggestion_list":suggestion_list,
        "form":form
    }
    return render(request, "index.html", context=context)

@login_required
def page(request):
    if request.method == "POST":
        form = forms.SuggestionForm(request.POST)
        if form.is_valid():
            form.save(request)
            form = forms.SuggestionForm()
    else:
        form = forms.SuggestionForm()
    suggestion_objects = models.Suggestion_Model.objects.all()
    suggestion_list=[]
    for sugg in suggestion_objects:
        comment_objects = models.CommentModel.objects.filter(suggestion=sugg)
        temp_sugg = {}
        temp_sugg["suggestion"]=sugg.suggestion
        temp_sugg["author"]=sugg.author.username
        temp_sugg["comments"]=comment_objects
        suggestion_list+=[temp_sugg]

    context = {
        "title":"Tempate Demo",
        "body":"<p> Hello Body</p>",
        "suggestion_list":suggestion_list,
        "form":form
    }
    return render(request, "index.html", context=context)

def register(request):
    if request.method == "POST":
        form_instance = forms.RegistrationForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect("/login/")
            # print("Hi")
    else:
        form_instance = forms.RegistrationForm()
    context = {
        "form":form_instance,
    }
    return render(request, "registration/register.html", context=context)