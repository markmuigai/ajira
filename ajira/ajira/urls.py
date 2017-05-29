from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'ajira.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('ajira_templates.urls')),
]
