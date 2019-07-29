from django.conf.urls import patterns, include, url
from django.contrib import admin
#from django.contrib import urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'savewise.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^carpooling/', include('carpooling.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
