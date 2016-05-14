from django.conf.urls import include, url
from django.contrib import admin

from .views import index, comments

urlpatterns = [
    # Examples:
    # url(r'^$', 'calendar_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', index, name='index'),
    url(r'^comments/$', comments, name='comments'),

    url(r'^admin/', include(admin.site.urls)),
]
