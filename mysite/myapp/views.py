from django.shortcuts import render, HttpResponse

from . import models

# Create your views here.
def index(request, page=0):
    suggestion_list = models.Suggestion_Model.objects.all()

    context = {
        "title":"Tempate Demo",
        "body":"<p> Hello Body</p>",
        "suggestion_list":suggestion_list
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
