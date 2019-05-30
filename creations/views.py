from django.shortcuts import render, get_object_or_404
from .models import Creation
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import creator_choices, category_choices


def creations(request):
    creations = Creation.objects.order_by(
        '-create_date').filter(is_published=True)

    paginator = Paginator(creations, 6)
    page = request.GET.get('page')
    paged_creations = paginator.get_page(page)

    context = {
        'creations': paged_creations
    }

    return render(request, 'creations/creations.html', context)


def creation(request, creation_id):
    creation = get_object_or_404(Creation, pk=creation_id)

    context = {
        'creation': creation
    }

    return render(request, 'creations/creation.html', context)


def search(request):

    queryset_list = Creation.objects.order_by('-create_date')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(
                description__icontains=keywords)
    # Creator
    if 'creator' in request.GET:
        creator = request.GET['creator']
        if creator:
            queryset_list = queryset_list.filter(
                creator__name__iexact=creator)

    # Category
    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            queryset_list = queryset_list.filter(
                category__iexact=category)

    context = {
        'creations': queryset_list,
        'creator_choices': creator_choices,
        'category_choices': category_choices,
        'values': request.GET
    }
    return render(request, 'creations/search.html', context)
