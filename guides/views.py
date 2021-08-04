from django.shortcuts import render
from .models import Guide

# Create your views here.


def all_guides(request):
    """ view to return all guides page """

    guides = Guide.objects.all()

    context = {
        'guides': guides,
    }

    return render(request, 'guides/guides.html', context)
