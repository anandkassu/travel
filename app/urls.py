from django.conf.urls import url
from django.contrib.auth import views
from django.views.generic.base import RedirectView
import app.views

urlpatterns = [
    # url(r'^$', app.views.home, name='home'),
    # url(r'^add', app.views.add, name='add'),
    url(r'^$', app.views.index, name='index'),

]