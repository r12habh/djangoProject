from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, 'home.html', {})


def about_view(request, *args, **kwargs):
    context = {
        'text': 'This is about us.',
        'number': 432534264,
        'list': [12, 23, 34, 'abc']
    }
    return render(request, 'about.html', context)


def contact_view(request, *args, **kwargs):
    return render(request, 'contact.html', {})


def social_view(request, *args, **kwargs):
    return render(request, 'social.html', {})
