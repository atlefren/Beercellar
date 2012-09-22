from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('beerlist.views',
    url(r'^$', 'index'),
    url(r'^style/(?P<type_id>\d+)/$', 'by_type'),
    url(r'^brewery/(?P<brewery_id>\d+)/$', 'by_brewery'),
    url(r'^country/(?P<country_id>\d+)/$', 'by_country'),
    url(r'^style/$', 'list_styles'),
    url(r'^brewery/$', 'list_breweries'),
    url(r'^country/$', 'list_countries'),
    url(r'^beer/(?P<beer_id>\d+)/drink/$', 'drink_beer'),
    url(r'^beer/(?P<beer_id>\d+)/add/$', 'add_beer'),
) 
