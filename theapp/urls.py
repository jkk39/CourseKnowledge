from django.conf.urls import url
from . import views

urlpatterns = [
	# /theapp/
    url(r'^$', views.index, name='index'),

    # /theapp/1234/
    # navigate to a view of school_id 1234
    url(r'^(?P<school_id>[0-9]+)/$', views.detail, name='detail'),
]