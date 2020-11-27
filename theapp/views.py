from django.http import Http404
from django.shortcuts import render
from .models import Student
from .models import School

def index(request):
	all_schools = School.objects.all()
	# create dictionary
	context = {
		'all_schools': all_schools,
	}
	return render(request, 'theapp/index.html', context)

	

def detail(request, school_id):
	try:
		school = School.objects.get(pk=school_id)	# check database for the school_id passed in
	except School.DoesNotExist:
		raise Http404("School not in Database")
	return render(request, 'theapp/detail.html', {'school': school,})


