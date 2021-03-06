"""TWDproject URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from registration.backends.default.views import RegistrationView
from rango.forms import UserProfileForm


class MyRegistrationView(RegistrationView):
    form_class = UserProfileForm
    def get_success_url(self, user):
        return '/rango/'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^rango/', include('rango.urls')),
    url(r'^accounts/register/$', MyRegistrationView.as_view(form_class = UserProfileForm), name='registration_register'),
    url(r'^accounts/', include('registration.backends.default.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""
As of Django 1.10, the patterns module has been removed (it had been deprecated since 1.8)

if settings.DEBUG:
    urlpatterns += patterns(
            'django.views.static',
            (r'media/(?P<path>.*)',
            'serve',
            {'document_root': settings.MEDIA_ROOT}),
    )
"""