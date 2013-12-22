from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import RequestContext, loader

from coins.models import Coin

# Create your views here.
def index(request):
    recently_added_coins_list = Coin.objects.order_by('-pub_date')[:5]
    template = loader.get_template('coins/index.html')
    context = {'recently_added_coins_list': recently_added_coins_list}
    return render(request, 'coins/index.html', context)

def view_collection(request):
    template = loader.get_template('coins/view_collection.html')
    context = {} 
    return render(request, 'coins/view_collection.html', context)

def coin(request, coin_id):
    coin = get_object_or_404(Coin, id=coin_id)
    return render(request, 'coins/detail.html', {'coin': coin})
