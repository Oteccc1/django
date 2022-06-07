from django.shortcuts import render
from .models import Block, Masters, Uslugi

def index(request):
    blocks = Block.objects.all()
    context = {
        'blocks': blocks,

    }
    return render(request, 'delote/index.html', context=context)

def masters(request):
    masters = Masters.objects.all()
    context = {
        'masters': masters,

    }
    return render(request, 'delote/masters.html', context=context)

def uslugi(request):
    uslugi = Uslugi.objects.all()
    context = {
        'uslugi': uslugi,
    }
    return render(request, 'delote/prices.html', context=context)

def location(request):
    return render(request, 'delote/location.html')
