from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, '../templates/home.html')

def about(request):
    return render(request, '../templates/about.html')

def work(request):
    return render(request, '../templates/work.html')

def contact(request):
    return render(request, '../templates/contact.html')
