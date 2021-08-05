from django.shortcuts import render, get_object_or_404
from .models import Guide

# Create your views here.


def all_guides(request):
    """ view to return all guides page """

    guides = Guide.objects.all()

    context = {
        'guides': guides,
    }

    return render(request, 'guides/guides.html', context)


def guide_detail(request, guide_id):
    """ view to return a page showing individual guide details """

    guide = get_object_or_404(Guide, pk=guide_id)

    context = {
        'guide': guide,
    }

    return render(request, 'guides/guide_detail.html', context)