from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import RequestContext, loader

from coins.models import Coin, Image

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
    
    template = loader.get_template('coins/view_collection.html')
    context = {'coins_list': coins_list} 
    return render(request, 'coins/view_collection.html', context)


def coin(request, coin_id):
    coin = get_object_or_404(Coin, id=coin_id)
    images_list = Image.objects.filter(coin=coin)
    context = {'coin': coin,
               'images_list': images_list,
               }
    return render(request, 'coins/detail.html', context)
