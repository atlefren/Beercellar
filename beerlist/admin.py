from beerlist.models import Beer,Brewery,BeerType,Country
from django.contrib import admin


class BeerAdmin(admin.ModelAdmin):
      fieldsets = [
            (None, {'fields': ['name', 'brewers', 'beer_type', 'ratebeerurl', 'abv', 'size', 'amount']}),
            ('Extra Information', {'fields': ['brewed', 'best_before', 'bought_date', 'batch', 'rating', 'price'], 'classes': ['collapse']})
      ]

admin.site.register(Beer, BeerAdmin)
admin.site.register(BeerType)
admin.site.register(Brewery)
admin.site.register(Country)