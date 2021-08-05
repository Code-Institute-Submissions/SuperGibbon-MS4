from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Guide

# Create your views here.


def all_guides(request):
    """ view to return all guides page """

    guides = Guide.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               "You didn't enter anything in the search box")
                return redirect(reverse('guides'))

            queries = Q(name__icontains=query) | Q(desciption__icontains=query)
            guides = guides.filter(queries)

    context = {
        'guides': guides,
        'search_term': query,
    }

    return render(request, 'guides/guides.html', context)


def guide_detail(request, guide_id):
    """ view to return a page showing individual guide details """

    guide = get_object_or_404(Guide, pk=guide_id)

    context = {
        'guide': guide,
    }

    return render(request, 'guides/guide_detail.html', context)
