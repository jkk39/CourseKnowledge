from django.http import HttpResponse
from django.template import loader
from .models import Student
from .models import School

def index(request):
	all_schools = School.objects.all()
	template = loader.get_template('theapp/index.html')
	# create dictionary
	context = {
		'all_schools': all_schools,
	}
	return HttpResponse(template.render(context, request))

	"""
	all_schools = School.objects.all()
	html = ''
	
	for school in all_schools:
		url = '/theapp/' + str(school.pk) + '/'
		html += '<a href="' + url + '">' + school.schoolname + '</a><br>'
	
	return HttpResponse(html)
	"""
	

def detail(request, school_id):
	return HttpResponse("<h2>Details for School ID:" + str(school_id) +  "</h2>")
