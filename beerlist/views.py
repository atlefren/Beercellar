# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.template import Context, loader
from beerlist.models import Beer,BeerType, Brewery,Country
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context import RequestContext
from django.core.urlresolvers import reverse


def index(request):
      beers = Beer.objects.all()
      num_liters = count_liters(beers) 
      sub = {}    
      return render_to_response('beerlist/index.html', context_instance=RequestContext(request, {'beers': beers,"sub": sub, "num_liters": num_liters}))
    
def by_type(request,type_id):
      beers = Beer.objects.filter(beer_type=type_id)
           
      type = BeerType.objects.get(id=type_id)      
      sub = {"name": type.name, "type": "Styles", "link": "style"}
      return render_to_response('beerlist/index.html', context_instance=RequestContext(request, {'beers': beers, "sub": sub}))
      
def by_brewery(request,brewery_id):
      beers = Beer.objects.filter(brewers=brewery_id)     
      brewery = Brewery.objects.get(id=brewery_id)      
      sub = {"name": brewery.name, "type": "Breweries", "link": "brewery"}
      return render_to_response('beerlist/index.html', context_instance=RequestContext(request, {'beers': beers, "sub": sub}))
      
def by_country(request,country_id):
      
      breweries = Brewery.objects.filter(country__id=country_id)
      beers = Beer.objects.filter(brewers__in=breweries)          
      country = Country.objects.get(id=country_id)      
      sub = {"name": country.name, "type": "Countries", "link": "country"}
      return render_to_response('beerlist/index.html', context_instance=RequestContext(request, {'beers': beers, "sub": sub}))
      
def list_styles(request):
      styles = BeerType.objects.all().order_by('name')     
      sub = {"type": "Styles", "link": "style"}
      return render_to_response('beerlist/objectlist.html', context_instance=RequestContext(request, {'objects': styles, "sub": sub}))
      
def list_breweries(request):
      breweries = Brewery.objects.all().order_by('name')        
      sub = {"type":"Breweries","link":"brewery"}      
      return render_to_response('beerlist/objectlist.html', context_instance=RequestContext(request, {'objects': breweries, "sub": sub}))

def list_countries(request):
      countries = Country.objects.all().order_by('name')        
      sub = {"type":"Countries","link":"country"}      
      return render_to_response('beerlist/objectlist.html', context_instance=RequestContext(request, {'objects': countries, "sub": sub}))

def drink_beer(request, beer_id):
      b = get_object_or_404(Beer, pk=beer_id)
      if b.amount > 0:
            b.amount -= 1
            b.save()
        
      return HttpResponseRedirect(reverse('beerlist.views.index'))      

def add_beer(request, beer_id):
      b = get_object_or_404(Beer, pk=beer_id)      
      b.amount += 1
      b.save()
        
      return HttpResponseRedirect(reverse('beerlist.views.index'))         
def count_liters(beers):
      num_liters = 0;
      for beer in beers:
            num_liters += beer.size*beer.amount;
      return num_liters
            
            
            
            
            
            
            