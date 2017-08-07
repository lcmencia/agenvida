"""agenvida URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static 
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from capitalario import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', views.authentication, name="authentication"),
    url(r'^logout/$', auth_views.logout, {'next_page': '/login'}, name="logout"),
    url(r'^$', views.purpose_list, name='list'),
    url(r'^(?P<id>\d+)/$', views.purpose_detail, name='detail'),
    url(r'^add/$', views.purpose_add, name='add'),
    url(r'^(?P<id>\d+)/edit/$', views.purpose_edit, name='edit'),
    url(r'^(?P<id>\d+)/delete/$', views.purpose_delete, name='delete'),
    url(r'^(?P<id>\d+)/contribute/$', views.PurposeContributeToggle.as_view(), name='contribute-toggle'),
    url(r'^password-change/$', views.password_change, name='password_change'),
    url(r'^password-change-done/$', views.password_change_done, name='password_change_done'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)