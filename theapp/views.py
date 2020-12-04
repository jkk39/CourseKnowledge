from django.http import Http404
from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Student
from .models import School
from .models import Friendship
from .models import Course
from .models import Professor
from .models import EnrollsIn

def index(request):
	all_schools = School.objects.all()
	# create dictionary
	context = {
		'all_schools': all_schools,
	}
	return render(request, 'theapp/index.html', context)

"""
class IndexView(generic.ListView):
	template_name = 'theapp/index.html'
	context_object_name = 'all_schools'

	def get_queryset(self):
		return School.objects.all()
"""
	

def detail(request, school_id):
	try:
		school = School.objects.get(pk=school_id)	# check database for the school_id passed in
	except School.DoesNotExist:
		raise Http404("School not in Database")
	return render(request, 'theapp/detail.html', {'school': school,})


class SchoolCreate(CreateView):
	models = School
	fields = ['schoolID', 'schoolname', 'address']
	template_name = 'theapp/school_form.html'

	def get_queryset(self):
		return School.objects.all()

class StudentCreate(CreateView):
    models = Student
    fields = ['school', 'studentID', 'name', 'GPA']
    template_name = 'theapp/student_form.html'

    def get_queryset(self):
        return Student.objects.all()

class CourseCreate(CreateView):
    models = Course
    fields = ['courseID', 'prof', 'coursename', 'credits']
    template_name = 'theapp/course_form.html'

    def get_queryset(self):
        return Course.objects.all()

class ProfessorCreate(CreateView):
    models = Professor
    fields = ['profID', 'profname', 'dept', 'school']
    template_name = 'theapp/professor_form.html'

    def get_queryset(self):
        return Professor.objects.all()

class EnrollsInCreate(CreateView):
    models = EnrollsIn
    fields = ['student', 'course', 'date', 'grade']
    template_name = 'theapp/enrollsin_form.html'

    def get_queryset(self):
        return EnrollsIn.objects.all()

class FriendCreate(CreateView):
    models = Friendship
    fields = ['friend1ID', 'friend2ID']
    template_name = 'theapp/friend_form.html'

    def get_queryset(self):
        return Friendship.objects.all()