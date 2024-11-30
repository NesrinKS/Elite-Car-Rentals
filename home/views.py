from django.shortcuts import render


def indexhome(request):
    return render(request, 'home/index.html')


def home_page(request):
    return render(request, 'home/firstpage.html')

def abouthome(request):
    return render(request,'home/aboutus.html')

def contacthome(request):
    return render(request,'home/contactus.html')






