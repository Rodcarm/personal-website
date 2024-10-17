from django.shortcuts import render, HttpResponse

print("Esto es un test para la carpeta core")
# Create your views here.
def home(request):
    return render(request, "core/home.html")

def about(request):
    print("final test")
    return render(request,"core/about.html")


def contact(request):
    return render(request,"core/contact.html")