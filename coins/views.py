import pdb
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import RequestContext, loader

from coins.models import Coin, Image, Corpus

# Create your views here.
def index(request):
    recently_added_coins_list = Coin.objects.order_by('-pub_date')[:5]
    images_list = Image.objects.all()
    template = loader.get_template('coins/index.html')
    context = {'recently_added_coins_list': recently_added_coins_list,
               'images_list': images_list}
    return render(request, 'coins/index.html', context)

def view_collection(request):
    if 'range' in request.GET:
        range = request.GET['range'].split(',');
        coins_list = Coin.objects.filter(date_start__gte=range[0]).filter(date_end__lte=range[1])
    else:
        coins_list = Coin.objects.all()

    images_list = []
    for coin in coins_list:
        image = Image.objects.filter(coin=coin)
        if len(image) > 0:
            images_list.append(image[0])
    
    template = loader.get_template('coins/view_collection.html')
    context = {'coins_list': coins_list,
               'images_list': images_list} 

    return render(request, 'coins/view_collection.html', context)

def view_corpora(request):
    corpora_list = Corpus.objects.all()

    template = loader.get_template('coins/view_corpora.html')
    context = {'corpora_list': corpora_list}

    return render(request, 'coins/view_corpora.html', context)

def coin(request, coin_id):
    coin = get_object_or_404(Coin, id=coin_id)
    images_list = Image.objects.filter(coin=coin)
    context = {'coin': coin,
               'images_list': images_list,
               }
    return render(request, 'coins/detail.html', context)

def corpus(request, coin_id):
    corpus = get_object_or_404(Corpus, id=corups_id)
    images_list = Image.objects.filter(corpus=corpus)
    context = {'corpus': corpus,
               'images_list': images_list,
               }
    return render(request, 'coins/corpus.html', context)
