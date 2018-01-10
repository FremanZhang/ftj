from django.conf.urls import url, include
import views


# the one in 1.7
# urlpatterns = patterns('',
#     url(r'^$', views.index, name='index')
# )

# The one in 1.11
#### [\w\-]+ presents one or more [number, char, _ or -]
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^category/(?P<category_slug_name>[\w\-]+/$)', views.category, name='category'),
]