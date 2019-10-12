from django.conf.urls import url
from django.contrib.auth import views
from django.views.generic.base import RedirectView
import app.views

urlpatterns = [
    # url(r'^$', app.views.home, name='home'),
    # url(r'^add', app.views.add, name='add'),
    url(r'^$', app.views.index, name='index'),
    url(r'^register', app.views.register, name='register'),
    url(r'^login', app.views.login, name='login'),
    url(r'^logout', app.views.logout, name='logout'),


]