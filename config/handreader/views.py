from django.shortcuts import render

# Create your views here.

def mainPage(request):
    if request.method == "POST":
        print("post")
    return render(request, 'upload.html')


