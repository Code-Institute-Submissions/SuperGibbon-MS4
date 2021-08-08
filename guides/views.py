from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q

from .models import Guide, Category
from .forms import GuideForm
from profiles.models import UserProfile

# Create your views here.


def all_guides(request):
    """ view to return all guides page """

    guides = Guide.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            guides = guides.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               "You didn't enter anything in the search box")
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
    if request.user.is_authenticated:
        profile = get_object_or_404(UserProfile, user=request.user)
        orders = profile.orders.all()
    else:
        orders = False

    context = {
        'guide': guide,
        'orders': orders,
    }

    return render(request, 'guides/guide_detail.html', context)


def add_guide(request):
    """
    Add guides to website
    """
    if request.method == 'POST':
        form = GuideForm(request.POST, request.FILES)
        if form.is_valid():
            guide = form.save()
            return redirect(reverse('guide_detail', args=[guide.id]))
    else:
        form = GuideForm

    form = GuideForm()
    template = 'guides/add_guide.html'
    context = {
        'form': form
    }

    return render(request, template, context)


def edit_guide(request, guide_id):
    """
    Edit a guide
    """
    guide = get_object_or_404(Guide, pk=guide_id)
    if request.method == 'POST':
        form = GuideForm(request.POST, request.FILES, instance=guide)
        if form.is_valid():
            form.save()
            return redirect(reverse('guide_detail', args=[guide.id]))
    else:
        form = GuideForm(instance=guide)

    template = 'guides/edit_guide.html'
    context = {
        'form': form,
        'guide': guide,
    }

    return render(request, template, context)


def delete_guide(request, guide_id):
    """
    Delete guide from store
    """
    guide = get_object_or_404(Guide, pk=guide_id)
    guide.delete()
    return redirect(reverse('guides'))
