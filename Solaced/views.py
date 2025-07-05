from django.shortcuts import render


def Home(request):
    return render(request, 'Homepage')
def About(request):
    return render(request, 'AboutPage')
def FAQ(request):
    return render(request, 'FAQPage')

