from django.shortcuts import render, HttpResponse


# Create your views here.
def home(request):
    print("view core")
    return render(request, "core/home.html")

def about(request):
    print("another test")
    return render(request,"core/about.html")


def contact(request):
    return render(request,"core/contact.html")