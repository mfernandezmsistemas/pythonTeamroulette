from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'teamroulette.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^test/$','teamroulette.views.test'),

    url(r'^admin/', include(admin.site.urls)),
)
