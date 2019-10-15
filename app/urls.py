from django.conf.urls import url
from django.contrib.auth import views
from django.views.generic.base import RedirectView
import app.views

urlpatterns = [
    # url(r'^$', app.views.home, name='home'),
    # url(r'^add', app.views.add, name='add'),
     url(r'^$', app.views.travel, name='travel'),
    url(r'^index', app.views.index, name='index'),
    url(r'^register', app.views.register, name='register'),
    url(r'^login', app.views.login, name='login'),
    # url(r'^accounts/login/?next=/index', app.views.login, name='login'),
    url(r'^logout', app.views.logout, name='logout'),
     url(r'^budget', app.views.home, name='home'),
    url(r'^contact', app.views.contact),
    url(r'^add_new', app.views.AddItemView.as_view()),
    url(r'^views', app.views.ListItemView.as_view()),
    url(r'^view/(?P<pk>\w+)/$', app.views.DetailItemView.as_view()),
    url(r'^view/(?P<pk>\w+)/edit/$', app.views.UpdateItemView.as_view()),
    url(r'^view/(?P<pk>\w+)/delete/$',app.views.DeleteItemView.as_view()),


]