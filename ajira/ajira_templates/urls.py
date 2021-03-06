"""aura_cms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf import settings
from . import views
#setting up the media
from django.conf.urls.static import static

urlpatterns = [
    # Login page
    url(r'^$', views.index, name='index'),
    url(r'^login_view/$', views.login_view, name='login_view'),
    url(r'^logout_view/$', views.logout_view, name='logout_view'),
    # Home page
    url(r'^home/$', views.home, name='home'),
    # Employer page
    url(r'^employer/$', views.employer, name='employer'),
    url(r'^employer_reg/$', views.employer_reg, name='employer_reg'),
    # Worker page
    url(r'^ajiriwa/$', views.ajiriwa, name='ajiriwa'),
    url(r'^ajiriwa_reg/$', views.ajiriwa_reg, name='ajiriwa_reg'),
    url(r'^register_ajiriwa/$', views.register_ajiriwa, name='register_ajiriwa'),
    url(r'^edit_profile/(?P<slug>[-\w]+)/$', views.edit_profile, name='edit_profile'),
    url(r'^simple_upload/$', views.simple_upload, name='simple_upload'),
    url(r'^ajiriwa_profile/(?P<slug>[-\w]+)/$', views.ajiriwa_profile, name='ajiriwa_profile'),
    url(r'^my_profile/(?P<slug>[-\w]+)/$', views.my_profile, name='my_profile'),
    # Job Page
    url(r'^post_job/$', views.post_job, name='post_job'),
    url(r'^view_job/$', views.view_job, name='view_job'),
    # Recommendations Page
    url(r'^recommend/$', views.recommend, name='recommend'),

]




#setting up the media file
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)