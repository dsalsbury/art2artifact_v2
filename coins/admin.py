from django.contrib import admin
from coins.models import Coin
from coins.models import Location
from coins.models import Corpus
from coins.models import coin_in_corpus

# Register your models here.
admin.site.register(Coin)
admin.site.register(Location)
admin.site.register(coin_in_corpus)
admin.site.register(Corpus)
