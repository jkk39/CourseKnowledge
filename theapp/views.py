from django.http import Http404
from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Student
from .models import School

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