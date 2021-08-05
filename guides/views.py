from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Guide, Category

# Create your views here.


def all_guides(request):
    """ view to return all guides page """

    guides = Guide.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                guides = guides.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            guides = guides.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            guides = guides.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter anything in the search box")
                return redirect(reverse('guides'))

            queries = Q(name__icontains=query) | Q(desciption__icontains=query)
            guides = guides.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'guides': guides,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'guides/guides.html', context)


def guide_detail(request, guide_id):
    """ view to return a page showing individual guide details """

    guide = get_object_or_404(Guide, pk=guide_id)

    context = {
        'guide': guide,
    }

    return render(request, 'guides/guide_detail.html', context)
