from django.conf.urls import patterns, url, include
import views


# the one in 1.7
# urlpatterns = patterns('',
#     url(r'^$', views.index, name='index')
# )

# The one in 1.11
urlpatterns = [
    url(r'^$', views.index, name='index'),
]