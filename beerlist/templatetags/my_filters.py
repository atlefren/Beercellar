from django import template

register = template.Library()

def print_names(brewers):
      n = brewers.count()
      if n==1:            
            return make_brewery_link(brewers[0])
      elif n ==2:
            return make_brewery_link(brewers[0]) + " & " + make_brewery_link(brewers[1])
      list = []      
      for brewer in brewers:
            list.append(make_brewery_link(brewer))
      return ", ".join(list)
      
def value_na(value):
      if value:
            return value
      return "N/A"
      
def two_dec(num):
      if num:
            return "%0.2f" % (num,)
      return num
      
def get_countries(brewers):
      countries = []
      for brewer in brewers:
            if not brewer.country in countries:
                  countries.append(brewer.country)
      markup = ""
      for country in countries:
            markup += "<a href='/beerlist/country/" + str(country.id) + "'><img src='blank.gif' class='flag flag-" + country.code + "' alt='" + country.name + "' /></a>"
      return markup

def make_brewery_link(brewery):  
      return "<a href='/beerlist/brewery/" + str(brewery.id) + "'>" + brewery.name + "</a>"
      
register.filter('print_names', print_names)      
register.filter('value_na', value_na)
register.filter('two_dec', two_dec)
register.filter('get_countries',get_countries)