from django.db import models
import django_tables2 as tables

class Country(models.Model):
      name = models.CharField(max_length=255)
      code = models.CharField(max_length=20)
      def __unicode__(self):
        return self.name
      
class Brewery(models.Model):
      name = models.CharField(max_length=255)
      country = models.ForeignKey(Country)
      def __unicode__(self):
        return self.name
      
class BeerType(models.Model):
      name = models.CharField(max_length=255)
      def __unicode__(self):
        return self.name
      
class Beer(models.Model):
      name = models.CharField('Beer Name', max_length=255)
      bought_date = models.DateField('Date Bought', blank=True, null=True)
      brewed = models.DateField('Brew date', blank=True, null=True)
      best_before = models.DateField('Best before', blank=True, null=True)
      batch = models.IntegerField('Batch #', blank=True, null=True)
      rating = models.IntegerField(blank=True, null=True)
      price = models.DecimalField('Price (NOK)', blank=True, null=True, max_digits=10, decimal_places=2)
      amount = models.IntegerField('Quantity', default=1)
      abv = models.DecimalField('ABV (%)', blank=True, null=True, max_digits=3, decimal_places=1)
      size =models.DecimalField('Volume (l)', blank=True, null=True, max_digits=4, decimal_places=2)
      ratebeerurl = models.CharField('RateBeer Link', max_length=255, blank=True, null=True)
      brewers = models.ManyToManyField(Brewery)
      beer_type = models.ForeignKey(BeerType)
      def __unicode__(self):
        return self.name      
