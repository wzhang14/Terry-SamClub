from django.shortcuts import render
from django.http import HttpResponse
from creations.choices import creator_choices, category_choices

from creations.models import Creation
from creators.models import Creator


def index(request):
    creations = Creation.objects.order_by(
        '-create_date').filter(is_published=True)[:3]

    context = {
        'creations': creations,
        'creator_choices': creator_choices,
        'category_choices': category_choices
    }

    return render(request, 'pages/index.html', context)


def about(request):
    creators = Creator.objects.order_by('name')

    mvp_creators = Creator.objects.all().filter(is_mvp=True)

    context = {
        'creators': creators,
        'mvp_creators': mvp_creators
    }

    return render(request, 'pages/about.html', context)
