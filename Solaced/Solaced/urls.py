from django.shortcuts import render


def Home(request):
    return render(request, 'HomePage.html')

def About(request):
    return render(request, 'AboutPage.html')

def FAQ(request):
    return render(request, 'FAQPage.html')