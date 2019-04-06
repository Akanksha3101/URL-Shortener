from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from django.urls import include, path

from shortener.views import HomeView, URLRedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view()),
    path('<shortcode>/', URLRedirectView.as_view(), name='scode'),
]
