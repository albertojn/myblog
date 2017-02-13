from django.conf.urls import include, url
from django.contrib import admin

from blog.views import IndexView, EntradaDetailView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
#    url(r'^markdown', include('django_markdown.urls')),

    url(r'^$', IndexView.as_view()),
    url(r'^entrada/(?P<slug>[-\w]+)/$', EntradaDetailView.as_view()),
]
