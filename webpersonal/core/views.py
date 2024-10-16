from django.shortcuts import render, HttpResponse


# Create your views here.
def home(request):
    return render(request, "core/home.html")

def about(request):
    print("se logro?")
    return render(request,"core/about.html")


def contact(request):
    print("final test")
    return render(request,"core/contact.html")