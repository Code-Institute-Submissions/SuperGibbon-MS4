from django.shortcuts import render
from guides.models import Guide

# Create your views here.


def index(request):
    """ view to return index page """

    guides = Guide.objects.all()
    template = 'home/index.html'
    context = {
        'guides': guides
    }

    return render(request, template, context)
