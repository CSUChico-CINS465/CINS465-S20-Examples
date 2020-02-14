from django.shortcuts import render, HttpResponse

from . import models
from . import forms

# Create your views here.
def index(request):
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

def page(request, page=0):
    my_list=[]
    for i in range(20):
        i+=(page*10+1)
        my_list+=[{
            "first_name": "Page"+str(i),
            "last_name": "Surname"+str(i),
            "cat":"https://images.pexels.com/photos/617278/pexels-photo-617278.jpeg"
            }
        ]
    context = {
        "title":"Tempate Demo",
        "body":"Hello Template",
        "temp_list":my_list[0:10]
    }
    return render(request, "index.html", context=context)
