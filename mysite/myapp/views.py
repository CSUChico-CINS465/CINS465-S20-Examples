# pylint: disable=W0703
from datetime import datetime, timezone
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import JsonResponse



from . import models
from . import forms





def logout_view(request):
    logout(request)
    return redirect("/")

def comment(request, sugg_id):
    if not request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        if request.user.is_authenticated:
            form = forms.CommentForm(request.POST)
            if form.is_valid():
                form.save(request, sugg_id)
                return redirect("/")
        else:
            form = forms.CommentForm()
    else:
        form = forms.CommentForm()
    context = {
        "title":"Comment",
        "sugg_id":sugg_id,
        "form":form
    }
    return render(request, "comment.html", context=context)

def make_suggestion(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            form = forms.SuggestionForm(request.POST, request.FILES)
            if form.is_valid():
                form.save(request)
                return redirect("/")
        else:
            form = forms.SuggestionForm()
    else:
        form = forms.SuggestionForm()
    context = {
        "title":"Add Suggestion",
        "form":form
    }
    return render(request, "suggestion.html", context=context)

# Create your views here.
def index(request):
    suggestion_objects = models.SuggestionModel.objects.all()
    suggestion_list = []
    for sugg in suggestion_objects:
        comment_objects = models.CommentModel.objects.filter(suggestion=sugg)
        temp_sugg = {}
        temp_sugg["suggestion"] = sugg.suggestion
        temp_sugg["author"] = sugg.author.username
        temp_sugg["comments"] = comment_objects
        suggestion_list += [temp_sugg]

    context = {
        "title":"Tempate Demo",
        "body":"<p> Hello Body</p>",
        "suggestion_list":suggestion_list,
    }
    return render(request, "index.html", context=context)



def get_suggestions(request):
    suggestion_objects = models.SuggestionModel.objects.all().order_by(
        '-published_on'
    )
    suggestion_list = {}
    suggestion_list["suggestions"] = []
    for sugg in suggestion_objects:
        comment_objects = models.CommentModel.objects.filter(
            suggestion=sugg
        ).order_by(
            '-published_on'
        )
        temp_sugg = {}
        temp_sugg["suggestion"] = sugg.suggestion
        temp_sugg["author"] = sugg.author.username
        temp_sugg["id"] = sugg.id
        try:
            temp_sugg["image"] = sugg.image.url
            temp_sugg["image_desc"] = sugg.image_description
        except Exception as err:
            print(err)
            temp_sugg["image"] = ""
            temp_sugg["image_desc"] = ""
        # except BaseException:
        #     temp_sugg["image"] = ""
        #     temp_sugg["image_desc"] = ""
        # except Exception as err:
        #     print(err)
        #     temp_sugg["image"] = ""
        #     temp_sugg["image_desc"] = ""
        temp_sugg["date"] = sugg.published_on.strftime("%Y-%m-%d %H:%M:%S")
        temp_sugg["comments"] = []
        for comm in comment_objects:
            temp_comm = {}
            temp_comm["comment"] = comm.comment
            temp_comm["id"] = comm.id
            temp_comm["author"] = comm.author.username
            temp_comm["date"] = datetime.now(timezone.utc) - comm.published_on
            # temp_comm["date"] = comm.published_on.strftime("%Y-%m-%d %H:%M:%S")
            temp_sugg["comments"] += [temp_comm]
        suggestion_list["suggestions"] += [temp_sugg]
    return JsonResponse(suggestion_list)

@login_required
def page(request):
    if request.method == "POST":
        form = forms.SuggestionForm(request.POST)
        if form.is_valid():
            form.save(request)
            form = forms.SuggestionForm()
    else:
        form = forms.SuggestionForm()
    suggestion_objects = models.SuggestionModel.objects.all()
    suggestion_list = []
    for sugg in suggestion_objects:
        comment_objects = models.CommentModel.objects.filter(suggestion=sugg)
        temp_sugg = {}
        temp_sugg["suggestion"] = sugg.suggestion
        temp_sugg["author"] = sugg.author.username
        temp_sugg["comments"] = comment_objects
        suggestion_list += [temp_sugg]

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
