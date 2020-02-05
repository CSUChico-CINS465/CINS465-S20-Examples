from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request, page=0):
    my_list=[]
    for i in range(20):
        i+=(page*10+1)
        my_list+=[{
            "first_name": "Name"+str(i),
            "last_name": "Surname"+str(i),
            "cat":"https://images.pexels.com/photos/617278/pexels-photo-617278.jpeg"
            }
        ]
    context = {
        "title":"Tempate Demo",
        "body":"<p> Hello Body</p>",
        "temp_list":my_list[0:10]
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
