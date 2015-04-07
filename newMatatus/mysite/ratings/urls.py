from django.conf.urls import patterns, url

from ratings import views

urlpatterns = patterns('',
    # ex: /ratings/
    url(r'^$', views.index, name='index'),
    url(r'about-us', views.about_us, name='about_us'),
    url(r'rate_form', views.rate_form, name='rate_form'),    
    url(r'rate', views.rate, name='rate'),        
)