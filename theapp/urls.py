from django.conf.urls import url
from . import views

# app_name is a namespace so we can reuse index and detail in other apps
app_name = 'theapp'

urlpatterns = [
	# /theapp/
    url(r'^$', views.index, name='index'),

    # /theapp/1234/
    # navigate to a view of school_id 1234
    url(r'^(?P<school_id>[0-9]+)/$', views.detail, name='detail'),

    # /theapp/school/add/
    url(r'school/add/$', views.SchoolCreate.as_view(), name='school-add'),

    #/theapp/student/add/
    url(r'student/add/$', views.StudentCreate.as_view(), name='student-add'),

    #/theapp/friend/add/
    url(r'friend/add/$', views.FriendCreate.as_view(), name='friend-add'),

    url(r'course/add/$', views.CourseCreate.as_view(), name='course-add'),

    url(r'enrollsin/add/$', views.EnrollsInCreate.as_view(), name='enrollsin-add'),

    url(r'professor/add/$', views.ProfessorCreate.as_view(), name='professor-add'),
]