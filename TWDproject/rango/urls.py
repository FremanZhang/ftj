from django.conf.urls import url
from . import views


# the one in 1.7
# urlpatterns = patterns('',
#     url(r'^$', views.index, name='index')
# )

# The one in 1.11
#### [\w\-]+ of (?P<category_name_slug>[\w\-]+) presents one or more [number, char, _ or -]
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
    url(r'^category/$', views.index, name='category_list'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
]